# Eine Variable ist ein benannter Speicherort für einen Wert
# Beispiel : 
name = "Fabio"
age = 25

# Du kannst den Wert einer Variable ändern
# Dafür verwenden wir verschiedene Operatoren
a = 10
b = 3
print(f"Addition: {a + b}")  # Addition
print("\n") # Neue Zeile
print(f"Subtraktion: {a - b}")  # Subtraktion
print("\n")
print(f"Multiplikation: {a * b}")  # Multiplikation
print("\n")
print(f"Division: {a / b}")  # Division (Ergebnis ist float)
print("\n")
print(f"Ganzzahl-Division: {a // b}") # Ganzzahl-Division
print("\n")
print(f"Rest: {a % b}")  # Rest
print("\n")

# Mit der input Funktion kannst du Benutzereingaben abfragen
user_name = input("Wie heißt du? ")
print(f"Hallo {user_name}")
print("\n")

# Standardmäßig ist die Eingabe immer ein String
# Deshalb müssen wir sie in eine Zahl umwandeln, wenn wir damit rechnen wollen
user_age = int(input("Wie alt bist du? "))
print(f"In 10 Jahren bist du: {user_age + 10}")
print("\n")

# ---Trinkgeld Rechner---
amount = float(input("Rechnungsbetrag in €: "))
tip = amount * 0.1
print(f"Trinkgeld (10%): {round(tip, 2)} €")
print("\n")

# ---Einheiten Umrechner---
km = float(input("Kilometer: "))
KM_TO_MILES = 0.621371
miles = km * KM_TO_MILES
print(f"{km} km sind {miles} Meilen")
print("\n")

# ---Fehler-Demo---
# Das folgende Beispiel zeigt, was passiert, wenn man KEINE Zahl eingibt.
# Probiere "zwanzig" statt 20 einzugeben:
age = int(input("Wie alt bist du? "))  # → ValueError

