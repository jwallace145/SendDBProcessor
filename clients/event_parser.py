from clients.logger import create_logger


class EventParser:

    def __init__(self, event: dict) -> None:
        self.event = event
        self.resource = event['resource']
        self.payload = self.parse_event(event)

        # create logger
        self.logger = create_logger(__name__)

        # log the event dictionary
        self.logger.info('event: %s', event)

    def parse_event(self, event: dict) -> dict:
        http_method = event['httpMethod']
        headers = event['headers']

        return {
            'http_method': http_method,
            'headers': headers
        }
