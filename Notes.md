Get token
curl -u u02sgb:password -kv -H "X-CSRF-Token: xxx" 'https://master.cluster.local:8443/oauth/authorize?client_id=openshift-challenging-client&response_type=token'


curl -u u02sgb:password -kv -H "X-CSRF-Token: xxx" 'https://<local-ip>/oauth/authorize?client_id=openshift-challenging-client&response_type=token'


location: https://<localip-port>/oauth/token/implicit#access_token=&expires_in=86400&scope=user%3Afull&token_type=Bearer

access_token=<TOKEN>

kubectl --token=<TOKEN> get pods -o name

import subprocess
subprocess.run(["kubectl", "--token=TOKEN "get", "pods", "-o=name"])

//Needs to be 3.8
temp = subprocess.run(["kubectl", "--token=TOKEN", "get", "pods", "-o=name"], capture_output=True)

my_pods = temp.stdout.split()

for i in my_pods:
  temp = subprocess.run(["kubectl", "--token=TOKEN", "logs", i], capture_output=True)
  print(temp.stdout)


History for Python3
import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))

ToDo
build docker file

docker build -t flask_log:latest
k8s deploy
service w htpasswd

https://docs.openshift.com/container-platform/4.1/authentication/identity_providers/configuring-htpasswd-identity-provider.html

htpasswd -c -B -b </path/to/users.htpasswd> <user_name> <password>
oc create secret generic htpass-secret --from-file=htpasswd=</path/to/users.htpasswd> -n openshift-config

apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
spec:
  identityProviders:
  - name: my_htpasswd_provider 
    mappingMethod: claim 
    type: HTPasswd
    htpasswd:
      fileData:
        name: htpass-secret 

https://kubernetes.github.io/ingress-nginx/examples/auth/basic/

Plan?
Setup a Route (as cert would be ok) add htpasswd to it
