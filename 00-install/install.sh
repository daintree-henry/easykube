# 클러스터 생성 시
kind create cluster --name easykube \
  --image kindest/node:v1.30.0 \
  --config kind-multi-node.yaml

# 매트릭 서버 설치
kubectl apply -f ./01-metric/metric-server.yaml

# 클러스터 삭제 시
kind delete cluster --name easykube