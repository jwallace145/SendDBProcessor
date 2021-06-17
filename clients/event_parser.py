import json
from clients.logger import create_logger


class EventParser:

    def __init__(self, event: dict) -> None:
        self.event = event
        self.resource = event['resource']
        self.payload = self.parse_event(event)

        # create logger
        self.logger = create_logger(__name__)

        # log the event dictionary
        self.logger.info('event resource: %s', self.resource)
        self.logger.info('event payload: %s', self.payload)

    def parse_event(self, event: dict) -> dict:
        http_method = event['httpMethod']
        headers = event['headers']
        path = self.parse_path(event)

        return {
            'http_method': http_method,
            'headers': headers,
            'path': path
        }

    def parse_path(self, event: dict) -> list:
        event_path = event['path']
        path = list(filter(None, event_path.split('/')))

        return path
