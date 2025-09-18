# --- Dateien ---
with open("todo.txt", "w") as f:
    f.write("Einkaufen\nWorkout\n")

with open("todo.txt", "r") as f:
    content = f.read()
    print("Inhalt von todo.txt:")
    print(content)

# --- JSON ---
import json

todos = ["Einkaufen", "Workout"]

with open("todos.json", "w") as f:
    json.dump(todos, f)

with open("todos.json", "r") as f:
    loaded = json.load(f)

print("Geladene Todos:", loaded)

# --- To-Do-Liste ---
todos = []
while True:
    task = input("Neue Aufgabe (oder 'fertig'): ")
    if task == "fertig":
        break
    todos.append(task)

with open("todos.json", "w") as f:
    json.dump(todos, f)

print("Aufgaben gespeichert!")

with open("todos.json", "r") as f:
    loaded = json.load(f)
    print("Geladene Aufgaben:", loaded)
