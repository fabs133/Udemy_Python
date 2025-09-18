# Strings: Textdaten in Anführungszeichen
first_name = "Fabio"
last_name = "Rempel"
print(first_name)
print(last_name)

# f-Strings: Variablen direkt in Text einfügen
print(f"Hallo, mein Name ist {first_name} {last_name}.")

# Methoden für Strings
name = "   Fabio  "
print(name.strip())   # entfernt Leerzeichen
print(name.lower())   # klein
print(name.upper())   # groß

text = "python kurs"
print(text.title())   # "Python Kurs"

# --- Begrüßungsformular ---
first = input("Vorname: ")
last = input("Nachname: ")
print(f"Hallo {first.strip().title()} {last.strip().title()}!")

# --- Initialen ---
initials = first[0] + last[0]  # String mit 1 Zeichen, kein "Char"
print(f"Deine Initialen sind: {initials.upper()}")
