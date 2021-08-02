import requests
import os
from dotenv.main import load_dotenv
load_dotenv()
API = os.getenv("RAPID_API")
import http.client

print("-------------------------")
x = input("Select your sports team:")
print("Sports team selected:", x)
print("Let me look that up for you...")


conn = http.client.HTTPSConnection("imdb8.p.rapidapi.com")

headers = {
    'x-rapidapi-key': API,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

conn.request("GET", "/auto-complete?q=", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

url = "https://imdb8.p.rapidapi.com/auto-complete"

querystring = {"q":x}

headers = {
    'x-rapidapi-key': API,
    'x-rapidapi-host': "imdb8.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
