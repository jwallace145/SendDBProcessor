import json
from models.climber import Climber
from clients.dynamodb_client import DynamoDBClient


class ClimbersProcessor:

    def __init__(self, dynamodb_client: DynamoDBClient) -> None:
        self.dynamodb_client = dynamodb_client

        # actions dictionary - contains http methods and their respective method to process the event
        self.actions = {
            'DELETE': self.delete_climber,
            'GET': self.get_climber,
            'PUT': self.put_climber
        }

    def process(self, payload: dict = {}) -> None:

        # get http method and headers from payload
        http_method = payload['http_method']
        headers = payload['headers']

        # call the appropriate method
        response = self.actions[http_method](headers)

        return response

    def delete_climber(self, headers):
        return 0

    def get_climber(self, headers):
        """ Handles all GET requests to climbers resource """
        climber_id = headers['climber_id']

        climber = self.dynamodb_client.get_climber(climber_id)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'status': 'successfully got a climber from climbers table'
            }),
            "isBase64Encoded": False
        }

    def put_climber(self, headers):

        # create climber
        climber = Climber(
            email=headers['email'],
            username=headers['username'],
            first_name=headers['first_name'],
            last_name=headers['last_name']
        )

        # put climber
        self.dynamodb_client.put_climber(climber)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'status': 'successfully inserted a climber into climbers table'
            }),
            "isBase64Encoded": False
        }