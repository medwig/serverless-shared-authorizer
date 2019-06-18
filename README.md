# Serverless shared authorizer example

Demonstrates how to use a shared custom authorizer across multiple services that share a single API Gateway.

The authorizer and the api gateway are defined in the `authorizer_and_api` service, and the `test_service` adds
a resource to that API, with the custom authorizer attached.

To run the demo:

```
$ cd authorizer_and_api/
$ sls deploy

$ cd ../test_service
$ sls deploy

$ curl https://apiroot.execute-api.us-east-1.amazonaws.com/dev/import_test -H 'Authorization:Bearer dev_token'
{"imported_authorizer": "example"}

$ curl https://apiroot.execute-api.us-east-1.amazonaws.com/dev/import_test -H 'Authorization:Bearer fake'     
{"Message":"User is not authorized to access this resource with an explicit deny"}
```

I can also demonstrate how to do the same with an API set up in Terraform, using SSM instead of Cloudformation Outputs, if there interest.


Sources:
- https://forum.serverless.com/t/share-authorizer-with-token-type/8121/9
- https://forum.serverless.com/t/shared-api-gateway-cognito-user-pools-authorizer-across-services/6565
- https://serverless.com/framework/docs/providers/aws/events/apigateway#http-endpoints-with-custom-authorizers

