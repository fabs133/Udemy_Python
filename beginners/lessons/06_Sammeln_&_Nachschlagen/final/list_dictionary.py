# --- Listen ---
todos = ["Einkaufen", "Workout", "Python lernen"]
print(todos)
print("Erste Aufgabe:", todos[0])

todos.append("Meditieren")
print("Nach append:", todos)

todos.pop()
print("Nach pop:", todos)

print("Anzahl Aufgaben:", len(todos))

print("Alle Aufgaben:")
for task in todos:
    print("-", task)

# --- Dictionaries ---
contact = {
    "name": "Fabio",
    "phone": "12345"
}
print("Name:", contact["name"])

contact["city"] = "Berlin"
print("Dictionary nach Hinzufügen:", contact)

if "phone" in contact:
    print("Telefonnummer:", contact["phone"])

print("Alle Schlüssel/Werte:")
for key in contact:
    print(key, ":", contact[key])

# --- To-Do-Liste ---
todos = []
while True:
    task = input("Neue Aufgabe (oder 'fertig'): ")
    if task == "fertig":
        break
    todos.append(task)

print("Deine Aufgaben:")
for t in todos:
    print("-", t)

# --- Kontaktbuch ---
contacts = {}
name = input("Name: ")
phone = input("Telefonnummer: ")
contacts[name] = phone

print("Gespeicherte Kontakte:")
for person in contacts:
    print(person, ":", contacts[person])
