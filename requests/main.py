# Request Library in Python
# url: https://www.youtube.com/watch?v=Xi1F2ZMAZ7Q
import requests


params ={
    "name": "Faraz",
    "age": 22
}

response = requests.get("https://httpbin.org/get", params=params)

print(response.status_code,"\n",response.text,"\n", response.json())