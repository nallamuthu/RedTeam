import requests
myurl = 'http://C2C-IP/index.php'
files = {'file': open('filename', 'rb')}
getdata = requests.post(myurl, files=files)
print(getdata.text)