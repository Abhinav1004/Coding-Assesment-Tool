#!/bin/bash
KUBECONTEXT="$(kubectl config current-context)"
echo $KUBECONTEXT
BRANCH=dev
aws ecr get-login-password --region eu-west-1 --profile dce | docker login --username AWS --password-stdin 938552122815.dkr.ecr.eu-west-1.amazonaws.com
docker buildx build --platform=linux/amd64 -t coding-assesment-tool:dev . --build-arg BRANCH=$BRANCH
docker tag coding-assesment-tool:dev 938552122815.dkr.ecr.eu-west-1.amazonaws.com/coding-assesment-tool:dev
docker push 938552122815.dkr.ecr.eu-west-1.amazonaws.com/coding-assesment-tool:dev
kubectl delete deployment coding-assesment-tool -n engines
kubectl apply -f deployment/deployment-dev.yaml -n engines
kubectl delete services coding-assesment-tool -n engines
kubectl apply -f deployment/services-dev.yaml -n engines
