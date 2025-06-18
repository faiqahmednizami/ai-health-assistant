def lambda_handler(event, context):
    user_input = event["inputTranscript"]
    return {
        "sessionAttributes": event.get("sessionAttributes", {}),
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "PlainText",
                "content": f"You asked about: {user_input}. (This is a placeholder response.)"
            }
        }
    }
