import json
from models.climber import Climber
from models.route import Route
from clients.dynamodb_client import DynamoDBClient

from clients.logger import create_logger


class ClimbersProcessor:

    def __init__(self, dynamodb_client: DynamoDBClient) -> None:
        self.dynamodb_client = dynamodb_client

        # actions dictionary - contains http methods and their respective method to process the event
        self.actions = {
            'DELETE': self.delete_climber,
            'GET': self.get_climber,
            'PUT': self.put_climber,
            'OPTIONS': self.get_options
        }

        # create logger
        self.logger = create_logger(__name__)

    def process(self, payload: dict = {}) -> None:

        # get http method
        http_method = payload['http_method']

        # call the appropriate method with payload as input
        response = self.actions[http_method](payload)

        return response

    def delete_climber(self, headers):
        """ Handles all DELETE requests to climbers resource """
        climber_id = headers['climber_id']

        climber = self.dynamodb_client.delete_climber(climber_id)

        self.logger.info(
            'this is the climber from the climbers processor %s', climber)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'status': 'successfully deleted a climber from the climbers table'
            }),
            "isBase64Encoded": False
        }

    def get_climber(self, payload: dict) -> dict:
        """ Handles all GET requests to climbers resource """
        if payload['path'][1] == 'sends':
            climber_email = payload['headers']['climber_email']

            climber_id = self.dynamodb_client.get_climber_by_email(
                climber_email)

            route_items = self.dynamodb_client.get_routes_by_climber_id(
                climber_id)

            routes = []
            for route_item in route_items:
                route = Route()
                route.initialize_from_db_item(route_item)
                routes.append(route.__dict__)

            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'numberOfSends': len(routes),
                    'routes': routes
                }),
                'isBase64Encoded': False
            }

        climber_id = payload['headers']['climber_id']

        climber = self.dynamodb_client.get_climber(climber_id)

        self.logger.info(
            'this is the climber obj from the climebrs processor class %s', climber)

        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(vars(climber)),
            "isBase64Encoded": False
        }

    def put_climber(self, headers):

        email = headers['email']

        # check for climber existence by email
        climber = self.dynamodb_client.get_climber_by_email(email)

        if climber:
            msg = f'climber with email {email} exists in the database'
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'status': msg
                }),
                'isBase64Encoded': False
            }

        username = headers['username']

        # check for climber existence by username
        climber = self.dynamodb_client.get_climber_by_username(username)

        if climber:
            msg = f'climber with username {username} exists in the database'
            return {
                'statusCode': 200,
                'headers': {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                },
                'body': json.dumps({
                    'status': msg
                }),
                'isBase64Encoded': False
            }

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
            'statusCode': 201,
            'headers': {
                'Location': climber.id,
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps(vars(climber)),
            'isBase64Encoded': False
        }

    def get_options(self, headers):
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Methods': '*'
            },
            'isBase64Encoded': False
        }
