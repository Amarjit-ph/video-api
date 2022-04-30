import json
from urllib import response
import requests

BASE = "http://127.0.0.1:5000"
list = [
    {
        "likes": 1256,
        "name": "Python REST API Tutorial - Building a Flask REST API",
        "views": 168955222
    },
    {
        "likes": 2526,
        "name": "Node REST API Tutorial - Building a Express REST API",
        "views": 1688888888
    },
    {
        "likes": 2574446,
        "name": "Go REST API Tutorial - Building a gin REST API",
        "views": 16888
    }
]


for i in range(len(list)):
    response = requests.put(BASE+"/video/"+str(i), list[i])
    print(response.json())

response = requests.delete(BASE+"/video/0")
print(response)

response1 = requests.get(BASE+"/video/1")
print(response1.json())

# response = requests.put(BASE+"/video/15678934", {
#     "likes": 256,
#     "name": "Python REST API Tutorial - Building a Flask REST API",
#     "views": 168955222
# })
# print(response.json())

# response = requests.get(BASE+"/video/156789345")
# print(response.json())
