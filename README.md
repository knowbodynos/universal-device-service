# universal-user-manual
Take a picture of any device, and get answers on how to operate it!

# Clone repo
```bash
git clone git@github.com:knowbodynos/universal-user-manual.git
cd universal-device-service
```

# Build and upload docker image
```bash
# Set variables
ECR_URL=""
REPO_NAME="universal-user-manual"
IMAGE_TAG="$(cat VERSION)"

# Switch to a docker buildx driver
docker buildx create --use

# Build docker image
docker buildx build --platform linux/amd64,linux/arm64 -t ${REPO_NAME}:${IMAGE_TAG} .

# Authenticate docker for AWS ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin ${ECR_URL}

# Tag image
docker tag ${REPO_NAME}:${IMAGE_TAG} ${ECR_URL}/${REPO_NAME}:${IMAGE_TAG}

# Push image to ECR
docker push ${ECR_URL}/${REPO_NAME}:${IMAGE_TAG}
```
