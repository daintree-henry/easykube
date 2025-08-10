# 클러스터 생성 시
kind create cluster --name easykube --config=kind-multi-node.yaml

# 매트릭 서버 설치
kubectl apply -f ./01-metric/metric-server.yaml

# Ingress Controller 설치
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.1/deploy/static/provider/cloud/deploy.yaml

# 클러스터 삭제 시
kind delete cluster --name easykube