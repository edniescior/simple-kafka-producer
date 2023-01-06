import pytest


@pytest.fixture(scope="module")
def lambda_context():
    class Context:
        def __init__(self) -> None:
            self.function_name = "test_lambda_handler"

    return Context()
