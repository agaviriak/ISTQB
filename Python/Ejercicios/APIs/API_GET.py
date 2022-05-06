import http.client

conn = http.client.HTTPSConnection("reqres.in")
payload = ''
headers = {}
conn.request("GET", "/api/users?id=5", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
