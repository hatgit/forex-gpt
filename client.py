import requests

data = {
    "instrument": "EUR_USD",
    "from_time": "2023-05-05T00:00:00.000000000Z",
    "granularity": "H1",
    "price": "M"
}

response = requests.post("http://localhost:5003/api/analyze", json=data)
print(response.json())