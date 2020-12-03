import json
import random
import datetime
from datetime import datetime

class Result():
    def __init__(self, attempts, name, date):
        self.attempts = score
        self.name = name
        self.date = date

myattempts = 0
myname=input("Bitte Namen eingeben: ")

def display_highscores(x=0, scores = []):
    print("-------------------------------------------------------------")
    print("High Scores:")
    with open("scores.json","r") as file:
        scores = json.loads(file.read())
        sort_scores = sorted(scores, key=lambda i: i['attempts'])
        while x < 3:
            entries = sort_scores[x]
            t=entries['date']
            t=datetime.strptime(t, '%Y-%m-%d %H:%M:%S.%f')
            print(f"{entries['name']}'s Score am {t.day}.{t.month}.{t.year}: {entries['attempts']}")
            x += 1
    print(f"Schaffst du es die Zahl mit weniger Versuchen zu erraten, {myname}?!")
    print("-------------------------------------------------------------")
    return scores

def write_scores_to_sheet(scores,attempts,current_time = datetime.now()):
    with open("scores.json", "w") as file:
        this_games_score = Result(attempts=myattempts, date=str(current_time), name=myname)
        scores.append(this_games_score.__dict__)
        file.write(json.dumps(scores))


def play_game(scores, secret=random.randint(1,30), attempts=0):
    print("-------------------------------------------------------------")
    guess = int(input(f"Bitte gib eine Zahl zwischen 1 und 30 ein, {myname}: "))
    lower_limit = 1
    upper_limit = 30
    while True:
        myattempts += 1
        if guess == secret:
            print(f"Gewonnen, {guess} war die richtige Zahl!")
            print(f"Du hast {attempts} Versuche gebraucht, {myname}!")
            write_scores_to_sheet(attempts=myattempts, scores=scores)
            break
        elif guess > secret:
            print(f"Die gesuchte Zahl ist kleiner als {guess}...")
            upper_limit=guess
            guess = int(input(f"Bitte gib eine Zahl, zwischen {lower_limit} und {guess} ein: "))

        elif guess < secret:
            print(f"Die gesuchte Zahl ist größer als {guess}...")
            lower_limit=guess
            guess = int(input(f"Bitte gib eine Zahl, zwischen {guess} und {upper_limit} ein: "))


play_game(scores=display_highscores())