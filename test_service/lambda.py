import json


def handler(event, context):
    result = {"imported_authorizer": "example"}
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": True,
    }
    return {"statusCode": 200, "headers": headers, "body": json.dumps(result)}
