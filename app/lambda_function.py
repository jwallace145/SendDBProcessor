import json

from models.climber import Climber

from clients.dynamodb_client import DynamoDBClient


def lambda_handler(event, context):

    dynamodb_client = DynamoDBClient()

    email = event['headers']['email']
    username = event['headers']['username']
    first_name = event['headers']['first_name']
    last_name = event['headers']['last_name']

    climber = Climber(
        email=email,
        username=username,
        first_name=first_name,
        last_name=last_name
    )

    dynamodb_client.put_climber(climber)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'status': 'another one'
        }),
        "isBase64Encoded": False
    }
