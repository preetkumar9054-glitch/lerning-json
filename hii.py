import json

response = requests.get("https://raw.githubusercontent.com/preetkumar9054-glitch/lerning-json/refs/heads/main/data.json")
data = response.json()

print(data)