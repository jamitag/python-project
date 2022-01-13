import requests
import random

def questions():
    response = requests.get("https://api.trivia.willfry.co.uk/questions?limit=5")
    return response.json()

def createAnswers(answers, correct):
    answers.append(correct)
    alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
    alphaList = alphabet.split()
    shuffledAnswers = random.sample(answers, len(answers))

    final = {}
    for answer in shuffledAnswers:
        i = shuffledAnswers.index(answer)
        final[alphaList[i]] = answer
    return final


def presentQuestion(q):
    print(q["question"])
    answers = createAnswers(q["incorrectAnswers"], q["correctAnswer"])
    for key, value in answers.items():
        line = key + ": " + value
        print(line)

if __name__ == "__main__":
    qs = questions()
    for q in qs:
        presentQuestion(q)




