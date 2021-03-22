import requests
r = requests.get("http://localhost:8000/Bike/")
r1 = requests.get("http://localhost:8000/RearWheel/")
r2 = requests.get("http://localhost:8000/FrontWheel/")

r = requests.post("http://127.0.0.1:8000/FrontWheel/", json={'bike': {'brand': 'Enve', 'size': '27', 'weight':10}
print(r.json())
print(r1.json())
print(r2.json())


