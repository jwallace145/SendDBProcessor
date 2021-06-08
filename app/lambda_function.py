import json

from clients.climbers_client import ClimbersClient


def lambda_handler(event, context):

    event_resource = event['resource']
    print(f'\n\nevent resource: {event_resource}')

    # initialize climbers client
    climbers_client = ClimbersClient(
        http_method=event['httpMethod'],
        headers=event['headers']
    )

    # process event
    response = climbers_client.process()

    return response
