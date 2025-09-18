# Cheatsheet – Lesson 6: Sammeln & Nachschlagen

## 📋 Listen
```python
todos = ["Einkaufen", "Workout"]
todos.append("Python")
todos.pop()
print(len(todos))
```

## 🔎 Iteration über Liste
```python
for task in todos:
    print(task)
```

## 📖 Dictionaries
```python
contact = {"name": "Fabio", "phone": "12345"}
print(contact["name"])

contact["city"] = "Berlin"
if "phone" in contact:
    print(contact["phone"])
```

## 🔁 Iteration über Dictionary
```python
for key in contact:
    print(key, ":", contact[key])
```

## ⚠️ Fehlerquellen
- Zugriff auf nicht existierenden Index → IndexError

- Zugriff auf nicht existierenden Schlüssel → KeyError