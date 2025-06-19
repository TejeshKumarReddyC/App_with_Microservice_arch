# Python application with microservices architecture
### Services used
1. ECR
2. ECS
3. Secret Manager
4. RDS
5. IAM
6. Cloudwatch

### Description
It consists of a python application that has frontend & backend containerized into two containers in the aws ecs, and automated the deployment with Github actions.   

### Workflow
Local repo --> Github --> Github Actions --> ECR --> ECS --> RDS
