import logging
from unittest.mock import MagicMock

import pytest
from kafka_producer.producer import SimpleKafkaProducer

@pytest.fixture
def simple_kafka_producer() -> SimpleKafkaProducer:
    obj = SimpleKafkaProducer.__new__(SimpleKafkaProducer)
    obj.logger = logging.getLogger("test_kafka_producer")
    obj.logger.setLevel(logging.DEBUG)
    obj.bootstrap_servers = 'dummy'
    obj.topic_name = 'wibble'
    obj.producer = MagicMock()
    return obj


def test_should_write_a_message_and_return_success(simple_kafka_producer):
    # GIVEN a single message
    # WHEN passed on to process event
    # THEN the message is sent to Kafka and a success notification is returned
    result = simple_kafka_producer.process_event("mary had a little lamb")
    assert simple_kafka_producer.producer.send.called
    assert simple_kafka_producer.producer.send.call_count == 1
    assert simple_kafka_producer.producer.send.call_args[0] == ('wibble', 'mary had a little lamb')
    assert result == {'body': 'mary had a little lamb', 'statusCode': 200}
