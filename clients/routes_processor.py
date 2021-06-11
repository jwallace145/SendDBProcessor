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
        http_method = payload['http_method']
        headers = payload['headers']

        response = self.actions[http_method](headers)

        return response

    def post_route(self, headers) -> None:

        # get climber by email
        climber = self.dynamodb_client.get_climber_by_email(
            email=headers['climber_email']
        )

        # get climber id
        climber_id = climber['id']['S']

        # create route
        route = Route(
            climber_id=climber_id,
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
