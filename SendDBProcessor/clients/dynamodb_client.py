import boto3
import datetime
import random
import sys

from ..models.climber import Climber
from .. import constants


class DynamoDBClient:

    def __init__(self, region: str = 'us-east-1') -> None:
        """ DynamoDB Client Constructor. """
        self.region = region

        # create dynamo db client
        self.client = boto3.client('dynamodb', region_name=region)

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

        print(key_dict)

        response = self.client.delete_item(
            TableName=table,
            Key=key_dict
        )

        return response

    def put_climber(self, climber: Climber) -> None:
        response = self.put_item(
            table=constants.CLIMBERS_TABLE,
            item=climber
        )

        return response

    def delete_climber(self, climber_id: str) -> None:
        response = self.delete_item(
            table=constants.CLIMBERS_TABLE,
            key=climber_id
        )

        return response
