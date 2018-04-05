import boto3

client = boto3.client(
    'iam',
    # Hard coded strings as credentials, not recommended.
    aws_access_key_id='AKIAIJEV6ANDOGVZLTAA',
    aws_secret_access_key='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'
)

print(client.list_users(PathPrefix='/'))