# Cheatsheet – Lesson 7: Funktionen

## 📝 Funktion definieren
```python
def greet(name):
    return f"Hallo {name}"
```

## 📞 Funktion aufrufen
```python
print(greet("Fabio"))
```

## ➕ Parameter & Rückgabewerte
```python
def add(a, b):
    return a + b
```

## 🌍 Scope
- Lokale Variablen → nur innerhalb der Funktion sichtbar

- Globale Variablen → überall sichtbar, aber mit Vorsicht nutzen

## 📖 Docstrings
```python
def clean_input(text):
    """Entfernt Leerzeichen und macht alles klein."""
    return text.strip().lower()
```    

## 🔑 Reine Funktion vs. I/O
- Rein: gleiche Eingabe → gleiche Ausgabe (len("abc"))

- I/O: wirkt auf die Außenwelt (print("Hallo"))