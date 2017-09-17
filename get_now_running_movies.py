import requests

conn = http.client.HTTPSConnection("api.themoviedb.org")

payload = "{}"

conn.request("GET", "/3/movie/now_playing?page=1&language=en-US&api_key=%3C%3Capi_key%3E%3E", payload)

res = conn.getresponse()
data = res.read()