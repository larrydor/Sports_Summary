import json
import re
import requests
import statistics
import requests
import os
from dotenv import dotenv_values
from dotenv.main import load_dotenv
load_dotenv()
API = os.getenv("RAPID_API")

print("-------------------------")
x = input("Select your sports team:")
print("Sports team selected:", x)
print("Let me look that up for you...")

sports_team = x

url = "https://api-basketball.p.rapidapi.com/timezone"

headers = {
    'x-rapidapi-key': API,
    'x-rapidapi-host': "api-basketball.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)


#r = requests.get(final_url)
#parsed_response = json.loads(r.text)