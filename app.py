from flask import Flask
import subprocess
import os
app = Flask(__name__)

pod_list=[]
token=""

@app.route('/')
def index():
    global pod_list, token
    #token= "62Vw-nCMoh08EKqtWNKY8pvGalLBvaZmONBeKrdGtFU"
    token= os.environ['K8S_TOKEN']
    temp = subprocess.run(["kubectl", f"--token={token}", "get", "pods", "-o=name"], capture_output=True)
    pod_list = temp.stdout.decode('utf-8').split()
    page_html = ['<html><h1>Log entries for Pods:</h1>']
    for idx, pod_name  in enumerate(pod_list):
        page_html.append(f'<a href="pod_logs/{idx}">{pod_name}</a><br>\n')
    page_html.append('</html>')
    return ''.join(page_html)

@app.route('/pod_logs/<int(min=0,max=99):pod_no>')
def pod_logs(pod_no):
    global pod_list, token
    if pod_no > len(pod_list):
        return "Error, invalid pod number"
    temp = subprocess.run(["kubectl", f"--token={token}", "logs", pod_list[pod_no]], capture_output=True)
    page_text = temp.stdout.decode('utf-8')
    page_text = ''.join(['<html>', '<pre>', page_text.replace('\\\\n', '<br />'), '</pre>', '</html>'])
    return page_text

if __name__ == '__main__':
    app.run(host='0.0.0.0')
