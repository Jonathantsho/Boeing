# Boeing
Data Engineer Boeing Interview - Christian Petro


## Built With

* [Flask](http://flask.pocoo.org/) - Python Microframework for API Development
* [API Gateway](https://aws.amazon.com/api-gateway/) - Scalable and efficient and managed service from AWS for deploying, maintaining, monitoring APIs
* [Lambda](https://aws.amazon.com/lambda/) - Serverless Compute Service
* [Serverless](https://serverless.com/) - Requirements & Service Provisioning, One click deployment
* [Jenkins](https://jenkins.io/) - for automatic testing before deployment.

## Why Serverless?
- Pay As You Go: When you don't need it, don't pay for it. 
- Favorable Pricing - about $3.50 per million on API Gateway and $0.20 per million for AWS Lambda.
- Infinite scale and high throughput - Lambda has no limit on the number of requests it can handle. The account limit on API Gateway is 10,000 requests per second or about 864M calls daily. This limit can be raised easily on the AWS Console, and you don't have to pay for how high the limit is, as the service is Pay As You Go.
- Fault Tolerant: No Maintenance, no scheduled down times. Maintains compute capacity across multiple Availability Zones in each region to help protect the code against individual machine or data center facility failures.

## Testing the API
GET - https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/dev
POST - https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/dev (send some raw string data to it, it'll say Hello {name} World!"
