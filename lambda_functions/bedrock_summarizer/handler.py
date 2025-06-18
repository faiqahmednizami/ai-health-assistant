import boto3
import json

def lambda_handler(event, context):
    client = boto3.client('bedrock-runtime')

    prompt = event.get("text", "Summarize this document:")
    modelId = "anthropic.claude-v2"

    body = {
        "prompt": f"Summarize this document: {prompt}",
        "max_tokens_to_sample": 300
    }

    response = client.invoke_model(
        modelId=modelId,
        contentType='application/json',
        body=json.dumps(body)
    )

    return {
        "statusCode": 200,
        "summary": response['body'].read().decode('utf-8')
    }
