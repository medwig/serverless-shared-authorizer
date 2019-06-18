""""
A lambda authorizer for an API KEY tokens.
"""

# $ head -c16 /dev/urandom | md5sum
DEV_TOKEN = "dev_token"


def generate_policy(effect, methodArn):
    principalId = "userid|placeholder"
    policyDocument = {
        "Version": "2012-10-17",
        "Statement": [
            {"Action": "execute-api:Invoke", "Effect": effect, "Resource": methodArn}
        ],
    }
    authResponse = {"principalId": principalId, "policyDocument": policyDocument}
    return authResponse


def handler(event, context):
    """Checks bearer token, calls use header format:
       'Bearer 22d9da'
    """
    token = event["authorizationToken"].split()[1]

    if token == DEV_TOKEN:
        print("Authenticated with dev token")
        return generate_policy("Allow", event["methodArn"])

    print("Access denied")
    return generate_policy("Deny", event["methodArn"])

