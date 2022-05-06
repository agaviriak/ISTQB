import http.client

conn = http.client.HTTPSConnection("reqres.in")
payload = "{\r\n\"name\":\"morpheus\",\r\n\"job\":\"leader\"\r\n}"
headers = {'Content-Type': 'text/plain'}
conn.request("POST", "/api/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
