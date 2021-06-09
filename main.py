from clients.dynamodb_client import DynamoDBClient

# create dynamodb client
dynamodb_client = DynamoDBClient()

climber = dynamodb_client.get_climber(
    climber_id='2021-06-06 19:48:50.384157T3074010271092525887')

print(climber)
