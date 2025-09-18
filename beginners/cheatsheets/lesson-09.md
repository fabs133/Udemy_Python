# Cheatsheet – Lesson 9: Dateien & JSON

## 📂 Dateien schreiben/lesen
```python
with open("todo.txt", "w") as f:
    f.write("Hallo Welt\n")

with open("todo.txt", "r") as f:
    content = f.read()
```

## 📄 Modi
- "w" → schreiben (überschreibt)

- "a" → anhängen

- "r" → lesen

## 📦 JSON speichern/laden
```python
import json

data = ["Eins", "Zwei"]

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "r") as f:
    loaded = json.load(f)
```

## ⚠️ Fehlerquellen
- Falscher Pfad → FileNotFoundError

- Datei überschrieben mit "w"

- JSON muss gültig sein, sonst json.JSONDecodeError