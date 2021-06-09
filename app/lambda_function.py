from clients.climbers_processor import ClimbersProcessor
from clients.routes_processor import RoutesProcessor
from clients.dynamodb_client import DynamoDBClient
from clients.event_parser import EventParser


def lambda_handler(event, context):

    # create dynamodb client
    dynamodb_client = DynamoDBClient()

    # create processors
    climbers_processor = ClimbersProcessor(dynamodb_client)
    routes_processor = RoutesProcessor(dynamodb_client)

    # create event parser
    event_parser = EventParser(event)

    # get event details
    resource = event_parser.resource
    payload = event_parser.payload

    # create resource processors switch dict
    processors = {
        '/{climbers+}': climbers_processor.process,
        '/{routes+}': routes_processor.process
    }

    # process the event
    response = processors[resource](payload)

    return response
