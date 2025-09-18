# Cheatsheet – Lesson 10: Module & Umgebungen

## 📦 Module importieren
```python
import math
print(math.sqrt(16))
print(math.pi)
```

## 🎲 Zufallszahlen
```python
import random
print(random.randint(1, 10))
```

## 📅 Datum/Zeit
```python
import datetime
print(datetime.date.today())
```

## 📥 Externe Pakete
```bash
pip install requests
```

## 🛡️ Virtuelle Umgebung
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

## 📝 Highscore-Beispiel
- Zufallszahl mit random.randint()

- Highscore in JSON-Datei speichern/laden