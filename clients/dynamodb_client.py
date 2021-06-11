import constants
from models.climber import Climber
from clients.logger import create_logger
import boto3
import datetime
import random
import sys
from boto3.dynamodb.conditions import Key
from models.route import Route


class DynamoDBClient:

    def __init__(self, region: str = 'us-east-1') -> None:
        """ DynamoDB Client Constructor. """
        self.region = region

        # create dynamo db client
        self.client = boto3.client('dynamodb', region_name=region)

        # create logger
        self.logger = create_logger(__name__)

    def put_item(self, table: str, item: object) -> None:

        # initialize item
        item_dict = {}

        # generate unique identifier
        item_id = str(datetime.datetime.utcnow()) + 'T' + \
            str(random.randint(0, sys.maxsize))

        item_dict['id'] = {
            'S': item_id
        }

        for key, value in vars(item).items():

            value_type = 'S'
            if isinstance(value, int):
                value_type = 'N'

            item_dict[key] = {
                value_type: value
            }

        response = self.client.put_item(
            TableName=table,
            Item=item_dict
        )

        return response

    def delete_item(self, table: str, key: str) -> None:
        """ Delete item """

        key_dict = {
            'id': {
                'S': key
            }
        }

        item = self.client.delete_item(
            TableName=table,
            Key=key_dict
        )

        return item

    def get_item(self, table: str, key: str) -> None:

        key_dict = {
            'id': {
                'S': key
            }
        }
        item = self.client.get_item(
            TableName=table,
            Key=key_dict
        )
        self.logger.info('this is the key dict %s', key_dict)
        self.logger.info('this is the item from the get item call %s', item)
        return item

    def get_climber_by_email(self, email: str) -> None:
        climber = self.client.query(
            TableName=constants.CLIMBERS_TABLE,
            IndexName='email-index',
            KeyConditionExpression='email = :email',
            ExpressionAttributeValues={
                ':email': {
                    'S': email
                }
            }
        )

        if len(climber['Items']) == 0:
            return None
        else:
            return climber

    def get_climber(self, climber_id: str) -> None:
        climber = self.get_item(table=constants.CLIMBERS_TABLE, key=climber_id)
        self.logger.info('get climber %s', climber)
        return climber

    def put_climber(self, climber: Climber) -> None:
        response = self.put_item(
            table=constants.CLIMBERS_TABLE,
            item=climber
        )

        return response

    def delete_climber(self, climber_id: str) -> None:
        climber = self.delete_item(
            table=constants.CLIMBERS_TABLE,
            key=climber_id
        )

        return climber

    def put_route(self, route: Route) -> None:
        response = self.put_item(
            table=constants.ROUTES_TABLE,
            item=route
        )

        return response
