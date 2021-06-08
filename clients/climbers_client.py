import json
from models.climber import Climber
from clients.clients import dynamodb_client


class ClimbersClient:

    def __init__(self, http_method: str = 'GET', headers: dict = {}) -> None:
        self.http_method = http_method
        self.headers = headers

        self.actions = {
            'DELETE': self.delete_climber(headers),
            'GET': self.get_climber(headers),
            'PUT': self.put_climber(headers)
        }

    def process(self):
        return self.actions[self.http_method]

    def delete_climber(self, headers):
        return 0

    def get_climber(self, headers):
        return 0

    def put_climber(self, headers):

        # create climber
        climber = Climber(
            email=headers['email'],
            username=headers['username'],
            first_name=headers['first_name'],
            last_name=headers['last_name']
        )

        # put climber
        dynamodb_client.put_climber(climber)

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
