import requests     # Install requests library

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

print(''':
ISS LIVE POSITION!
''')

print(f"Latitude: {data['iss_position']['latitude']}")
print(f"Longitude: {data['iss_position']['longitude']}\n")
