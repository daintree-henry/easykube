# 1. Ingress Controller 설치
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.12.1/deploy/static/provider/cloud/deploy.yaml

# 2. Ingress Controller가 정상적으로 설치되었는지 확인
kubectl get all -n ingress-nginx
kubectl get po -n ingress-nginx -w

# 3. 로컬 환경에서 사용하기 위해 admission webhook 삭제
kubectl delete validatingwebhookconfiguration ingress-nginx-admission



