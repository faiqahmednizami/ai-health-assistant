import boto3
import json

def lambda_handler(event, context):
    s3_bucket = event["Records"][0]["s3"]["bucket"]["name"]
    s3_key = event["Records"][0]["s3"]["object"]["key"]

    textract = boto3.client('textract')
    response = textract.analyze_document(
        Document={'S3Object': {'Bucket': s3_bucket, 'Name': s3_key}},
        FeatureTypes=["FORMS"]
    )

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }
