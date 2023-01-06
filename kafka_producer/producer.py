import logging
import os
import json

from layers.decorators import notify_cloudwatch
from kafka import KafkaProducer


logging.basicConfig(format="%(asctime)s %(name)s %(levelname)s %(message)s")
logger = logging.getLogger("SimpleKafkaProducer")
logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))


class SimpleKafkaProducer:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(os.environ.get("LOGGING", logging.DEBUG))

        self.bootstrap_servers = os.environ.get("KAFKA_BOOTSTRAP_SERVERS", 'localhost:9092')
        self.logger.info(f"{self.bootstrap_servers=}")

        self.topic_name = os.environ.get("KAFKA_TOPIC_NAME", 'unset')
        self.logger.info(f"{self.topic_name=}")

        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers)

    def process_event(self, event):
        response = self.producer.send(self.topic_name, event)
        self.logger.info(f"{response=}")
        return {
            "statusCode": 200,
            "body": json.dumps({
                "result": "from Producer"
            }),
        }


@notify_cloudwatch
def handler(event, context):
    return SimpleKafkaProducer().process_event(event)


if __name__ == "__main__":
    pass
