"# dbs-ui-app" 





 kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.21/samples/addons/kiali.yaml


 helm repo add kiali https://kiali.org/helm-charts

helm install \
    --set cr.create=true \
    --set cr.namespace=istio-system \
    --set cr.spec.auth.strategy="anonymous" \
    --namespace kiali-operator \
    --create-namespace \
    kiali-operator \
    kiali/kiali-operator


 helm install kubefirst --namespace kubefirst --create-namespace  kubefirst/kubefirs
  kubectl -n kubefirst port-forward svc/kubefirst-console 8080:8080
  
 kubectl patch svc kubefirst-console -n kubefirst -p '{"spec": {"ports": [{"port": 8080,"targetPort": 8080,"name": "https"}],"type": "LoadBalancer"}}'


 ##role outs

 kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml



curl -L https://istio.io/downloadIstio | sh -
cd istio-<version-number>
export PATH=$PWD/bin:$PATH
istioctl install --set profile=demo -y