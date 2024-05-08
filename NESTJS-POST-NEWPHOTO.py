import requests
import json

url = "http://localhost:3000/photo"

payload = json.dumps({
  "name": "Otra foto mas",
  "description": "Esta es otra foto de prueba",
  "filename": "ejemplo7.jpeg",
  "views": "0",
  "isPublished": True
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.e30.eMJ6tbXpt_mqIaZze4qHiHDljE-EkHt4wFuG2nvds5A'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)