import requests

response = requests.get("https://api.trivia.willfry.co.uk/questions?limit=5")

print(response.json())

