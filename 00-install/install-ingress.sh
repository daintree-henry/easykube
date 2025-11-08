# 1. Ingress Controller 설치
cd ~/easykube/00-install
kubectl apply -f ingress-controller.yaml

# 2. Ingress Controller가 정상적으로 설치되었는지 확인
kubectl get all -n ingress-nginx
kubectl get po -n ingress-nginx -w

# 3. 로컬 환경에서 사용하기 위해 admission webhook 삭제
kubectl delete validatingwebhookconfiguration ingress-nginx-admission



