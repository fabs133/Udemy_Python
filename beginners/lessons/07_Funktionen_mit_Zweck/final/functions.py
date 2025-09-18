# Funktion nutzen
def greet(name):
    return f"Hallo {name}!"

print(greet("Fabio"))

# Funktion mit zwei Parametern
def add(a, b):
    return a + b

print("Addition:", add(2, 3))

# Scope: lokal vs. global
def test():
    x = 42
    print("Innerhalb der Funktion:", x)

test()
# print(x)  # Fehler: x ist nicht global sichtbar

# Funktion mit Docstring
def clean_input(text):
    """
    Entfernt Leerzeichen und gibt den Text in Kleinbuchstaben zurück.
    """
    return text.strip().lower()

user = input("Gib etwas ein: ")
print("Bereinigt:", clean_input(user))

# Challenge: Passwort-Check
def is_strong_password(pw):
    """
    Prüft, ob Passwort mindestens 8 Zeichen lang ist und eine Zahl enthält.
    """
    return len(pw) >= 8 and any(char.isdigit() for char in pw)

print(is_strong_password("abc123"))  # False
print(is_strong_password("superpasswort1"))  # True
