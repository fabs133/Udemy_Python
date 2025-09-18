# for mit range
for i in range(5):
    print("Hallo", i)

# Iteration über Liste
fruits = ["Apfel", "Banane", "Kirsche"]
for fruit in fruits:
    print(fruit)

# Iteration über String
text = "Python"
for letter in text:
    print(letter)

# while mit Abbruchbedingung
count = 0
while count < 5:
    print("Zahl:", count)
    count += 1

# --- Zahlraten ---
secret = 7
guess = None

while guess != secret:
    guess = int(input("Rate eine Zahl von 1 bis 10: "))

print("Richtig!")

# --- Multiplikationstafel ---
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
