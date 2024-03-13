def lambda_handler(event, context):
    # Respond with a 200 OK status and a message indicating the service is healthy
    return {
        'statusCode': 200,
        'body': 'Service is healthy'
    }