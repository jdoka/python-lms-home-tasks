import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.headers)
print(response.json()[0:5])
