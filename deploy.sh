zip -r test-lambda.zip .

aws lambda create-function \
    --function-name test-lambda-function \
    --runtime python3.8 \
    --role arn:aws:iam::650503560686:role/LambdaAdminAccess \
    --handler lambda_function.lambda_handler \
    --zip-file fileb://test-lambda.zip