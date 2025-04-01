import boto3

s3_client = boto3.client(
    "s3",
    endpoint_url=f"http://localhost.localstack.cloud:4566",
    aws_access_key_id="MockAccessKeyId",
    aws_secret_access_key="MockSecretAccessKey"
)

s3_client.create_bucket(
    Bucket="amplify-bucket",
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    }
)