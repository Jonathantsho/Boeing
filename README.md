# Boeing
Data Engineer Boeing Interview - Christian Petro


## Built With

* [Flask](http://flask.pocoo.org/) - Python Microframework for API Development
* [API Gateway](https://aws.amazon.com/api-gateway/) - Scalable and efficient and managed service from AWS for deploying, maintaining, monitoring APIs
* [Lambda](https://aws.amazon.com/lambda/) - Serverless Compute Service
* [Serverless](https://serverless.com/) - Requirements & Service Provisioning, One click deployment
* [Jenkins](https://jenkins.io/) - for automatic testing before deployment.
* [Git](https://github.com/) - For launching, debugging, and testing specific versions of the service

## Why Serverless?
- Pay As You Go: When you don't need it, don't pay for it. 
- Favorable Pricing - about $3.50 per million on API Gateway and $0.20 per million for AWS Lambda. versus non-linear pricing with EMR Clusters / Elastic Beanstalk (server sided)
- Infinite scale and high throughput - Lambda has no limit on the number of requests it can handle. The account limit on API Gateway is 10,000 requests per second or about 864M calls daily. This limit can be raised easily on the AWS Console, and you don't have to pay for how high the limit is, as the service is Pay As You Go.
- Fault Tolerant: No Maintenance, no scheduled down times. Maintains compute capacity across multiple Availability Zones in each region to help protect the code against individual machine or data center facility failures.

## Testing the API
- GET - https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/prod
- POST - https://r0xybgunmj.execute-api.us-east-1.amazonaws.com/prod (send some raw string data to it, it'll say Hello {name} World!"
- To change existing environments, simply change "prod" in the URL to "dev", "test", "demo"

## Test Questions

### Ensure that changes to the source code can be automatically tested before they are deployed 
- This is done with Jenkins, I've built in a api unittest that will check the Flask API that I hosted on AWS before each deployment. 
- I've hosted Jenkins on an EC2 Amazon Linux AMI Server. 
- You can find a sample of the unittest output in (https://github.com/Jonathantsho/Boeing/blob/master/Jenkin%20Log%20File%20Example)

### Specific version of the service can be launched for testing, debugging and demos
This is done with Git.

### Infrastructure and required services provisioning as well as deployment is automated and can be triggered with a click of a button or a command in a terminal.
This is done with Serverless Framework, which allows extremely easy deployment from local to cloud within one command.
```
serverless deploy
```
For more info, check here https://serverless.com/framework/docs/providers/aws/guide/deploying/

### Service is reasonably resilient and a single node failure does not affect end users 
AWS Lambda is fully managed and has built in replication across many data centers which will protect it from single node failures.

### Service can be scaled, preferably automatically, to handle increased loads 
AWS Lambda Auto-scales to infinity given the number of requests.
AWS API Gateway has a current capacity of 10,000 requests per second, but this can be changed via a simple support request to upgrade to 50,000 requests if you'd like. This is also free, as API gateway is pay as you go. 

