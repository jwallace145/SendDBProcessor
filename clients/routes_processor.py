from clients.dynamodb_client import DynamoDBClient


class RoutesProcessor:

    def __init__(self, dynamodb_client: DynamoDBClient) -> None:
        self.dynamodb_client = dynamodb_client

    def process(self, payload) -> None:
        return 0
