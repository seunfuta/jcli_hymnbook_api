import requests

#print(requests.get('http://localhost:8000').json())

#print(requests.get('http://localhost:8000/hymns/1').json())

#print(requests.get('http://localhost:8000/hymns?language=english'))

#print(requests.get('http://localhost:8000/filterx?language=english').json())

response = requests.get('http://localhost:8000/filterx?verses=of%20patient%20hope%20and%20quiet,%20brave%20endurance,').json()
print(response)  # Print the raw response text
