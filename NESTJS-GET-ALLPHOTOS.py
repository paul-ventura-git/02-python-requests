import requests
import json

url = "http://localhost:3000/photo"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.e30.eMJ6tbXpt_mqIaZze4qHiHDljE-EkHt4wFuG2nvds5A'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
