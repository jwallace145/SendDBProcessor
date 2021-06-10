from clients.dynamodb_client import DynamoDBClient

# create dynamodb client
dynamodb_client = DynamoDBClient()

climber = dynamodb_client.get_climber_by_email(
    email="alex.honnold@gmail.com1"
)

if len(climber['Items']) == 1:
    print(climber)
