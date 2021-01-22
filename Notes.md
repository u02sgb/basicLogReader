Get token
curl -u u02sgb:password -kv -H "X-CSRF-Token: xxx" 'https://master.cluster.local:8443/oauth/authorize?client_id=openshift-challenging-client&response_type=token'


curl -u u02sgb:password -kv -H "X-CSRF-Token: xxx" 'https://192.168.2.33/oauth/authorize?client_id=openshift-challenging-client&response_type=token'


location: https://192.168.2.33:8443/oauth/token/implicit#access_token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU&expires_in=86400&scope=user%3Afull&token_type=Bearer

access_token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU

kubectl --token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU get pods -o name

import subprocess
subprocess.run(["kubectl", "--token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU", "get", "pods", "-o=name"])

//Needs to be 3.8
temp = subprocess.run(["kubectl", "--token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU", "get", "pods", "-o=name"], capture_output=True)

my_pods = temp.stdout.split()

for i in my_pods:
  temp = subprocess.run(["kubectl", "--token=62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU", "logs", i], capture_output=True)
  print(temp.stdout)


History for Python3
import readline; print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))

