docker build -t devwikirepo/probe-practice:1.6 .
docker push devwikirepo/probe-practice:1.6
docker run --rm -p 5000:5000 devwikirepo/probe-practice:1.6

curl localhost:5000/startupz  
curl localhost:5000/readyz    
curl localhost:5000/healthz   
