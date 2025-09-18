# Cheatsheet – Lesson 8: Fehler verstehen & handhaben

## 🚨 Exceptions
- Fehler heißen in Python **Exceptions**
- Beispiele: `ZeroDivisionError`, `ValueError`

## 🔒 try/except
```python
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Durch null teilen geht nicht!")
```

## ➕ else & finally
```python
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Fehler!")
else:
    print("Kein Fehler:", x)
finally:
    print("Läuft immer.")
```

## 🛡️ Defensive Programmierung
- Sichere Division:
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

- Robuste Eingabe:
```python
while True:
    try:
        num = int(input("Zahl: "))
        break
    except ValueError:
        print("Bitte eine gültige Zahl!")
```

## ⚠️ Fehlerquellen
- except: fängt alles – besser spezifizieren

- Endlosschleife bei Eingaben möglich → mit break beenden