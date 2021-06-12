from app.lambda_function import lambda_handler
import json
from argparse import ArgumentParser
from clients.logger import create_logger


def main():

    # create logger
    logger = create_logger(__name__)

    # create cli arg parser
    parser = ArgumentParser()
    parser.add_argument('positionals', nargs='*')
    args = parser.parse_args()

    # get event file name
    event_file_name = args.positionals[0]

    logger.info(
        'event file name retrieved from command line argument %s', event_file_name)

    # open event file
    with open(f'tests/events/{event_file_name}.json', 'r') as file:
        event = json.loads(file.read())

    response = lambda_handler(event, {})

    logger.info('the json response from the lamdba:\n%s',
                json.dumps(response, indent=2))

    return


if __name__ == '__main__':
    main()
