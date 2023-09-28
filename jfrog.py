
import subprocess,os,requests

jfrog_token="AKCp8pR638bwXJZwrviQhjRm9ZrdxyVg2NodsFiezwWPyeNDhE1bnY5jpQwYffaAtPDQpy9ri"
url="http://34.203.38.217:8082/artifactory/example-repo-local/python/kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar"
jar_file_path='kubernetes-configmap-reload-0.0.1-SNAPSHOT.jar'

header={
    'X-JFrog-Art-Api':"AKCp8pR638bwXJZwrviQhjRm9ZrdxyVg2NodsFiezwWPyeNDhE1bnY5jpQwYffaAtPDQpy9ri"
}
try:
    
    with open(jar_file_path,'rb') as jar_file:
        jar_file_contents=jar_file.read()
        result=requests.put(url,headers=header,data=jar_file)
    print(result.json())
except subprocess.CalledProcessError as e:
    print("curl command failed with error:",e)

if (result.status_code==201):
    print("uploaded successfully")
else:
    print(result.status_code)

