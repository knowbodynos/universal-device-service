# universal-device-service
App for universal device technical service

# Clone repo
```bash
git clone git@github.com:knowbodynos/universal-device-service.git
cd universal-device-service
```

# Build and upload docker image
```bash
# Set variables
ECR_URL="507089137074.dkr.ecr.us-east-1.amazonaws.com"
REPO_NAME="universal-device-service"
IMAGE_TAG="$(cat VERSION)"

# Switch to a docker buildx driver
docker buildx create --use

# Build docker image
docker buildx build --platform linux/amd64,linux/arm64 -t ${REPO_NAME}:${IMAGE_TAG} .

# Authenticate docker for AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 507089137074.dkr.ecr.us-east-1.amazonaws.com

# Tag image
docker tag ${REPO_NAME}:${IMAGE_TAG} ${ECR_URL}/${REPO_NAME}:${IMAGE_TAG}

# Push image to ECR
docker push ${ECR_URL}/${REPO_NAME}:${IMAGE_TAG}
```