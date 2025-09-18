# Volljährigkeit prüfen
age = int(input("Wie alt bist du? "))

if age >= 18:
    print("Du bist volljährig")
else:
    print("Du bist minderjährig")

# Noten-Beispiel
grade = int(input("Note (1-5): "))

if grade == 1:
    print("Sehr gut")
elif grade == 2:
    print("Gut")
elif grade == 3:
    print("Befriedigend")
else:
    print("Verbesserungswürdig")

# Preisrechner mit Rabatt
price = float(input("Betrag in €: "))

if price > 100:
    discount = price * 0.1
    price -= discount
    print(f"Rabatt gewährt: {discount} €")
else:
    print("Kein Rabatt")

print(f"Endpreis: {price} €")

# Passwort-Check
pw = input("Passwort: ")

if len(pw) >= 8 and any(char.isdigit() for char in pw):
    print("Passwort akzeptiert")
else:
    print("Passwort zu schwach")
