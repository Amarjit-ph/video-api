import requests

BASE = "http://127.0.0.1:5000"
list = [
    {
        "likes": 1256,
        "name": "Python REST API Tutorial - Building a Flask REST API",
        "views": 168955222
    },
    {
        "likes": 1256,
        "name": "Python REST API Tutorial - Building a Flask REST API",
        "views": 168955222
    },
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


# for i in range(len(list)):
#     response = requests.put(BASE+"/video/"+str(i), list[i])
#     print(response.json())

response1 = requests.get(BASE+"/video/0")
response2 = requests.get(BASE+"/video/1")
response3 = requests.get(BASE+"/video/2")
print(response1.json())
print(response2.json())
print(response3.json())
