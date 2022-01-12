import requests

response = requests.get("https://api.trivia.willfry.co.uk/questions?limit=5")

questions = response.json()

print(questions[0]["question"])