import math
import random
import datetime
import json

# --- Beispiele mit Standardbibliothek ---
print("Quadratwurzel von 16:", math.sqrt(16))
print("Pi:", math.pi)
print("Zufallszahl (1-6):", random.randint(1, 6))
print("Heutiges Datum:", datetime.date.today())

# --- Zahlraten mit Highscore ---
secret = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Rate die Zahl (1-10): "))
    attempts += 1
    if guess == secret:
        print("Richtig in", attempts, "Versuchen!")
        break
    else:
        print("Falsch, versuch's nochmal!")

# Highscore laden
try:
    with open("highscore.json", "r") as f:
        highscore = json.load(f)
except FileNotFoundError:
    highscore = None

# Highscore prüfen und ggf. speichern
if highscore is None or attempts < highscore:
    print("Neuer Highscore:", attempts)
    with open("highscore.json", "w") as f:
        json.dump(attempts, f)
else:
    print("Bester Highscore bleibt:", highscore)
