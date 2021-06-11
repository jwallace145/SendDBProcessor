import json

from models.route import Route

from clients.dynamodb_client import DynamoDBClient


class RoutesProcessor:

    def __init__(self, dynamodb_client: DynamoDBClient) -> None:
        self.dynamodb_client = dynamodb_client

        self.actions = {
            'POST': self.post_route
        }

    def process(self, payload) -> None:
        return 0

    def post_route(self, headers) -> None:

        # create route
        route = Route(
            climber_email=headers['climber_email'],
            name=headers['name'],
            grade=headers['grade'],
            type=headers['type'],
            crag=headers['crag'],
            style=headers['style'],
            ascent=headers['ascent'],
            height=headers['height'],
            pitches=headers['pitches']
        )

        # put route
        self.dynamodb_client.put_route(route)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'status': 'successfully inserted a route into the database. nice send brah'
            }),
            'isBase64Encoded': False
        }
