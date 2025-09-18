# Cheatsheet – Lesson 4: Entscheidungen treffen

## 🔑 If-Statements
```python
if age >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

## 🔄 Mehrere Bedingungen
```python
if x == 1:
    print("Eins")
elif x == 2:
    print("Zwei")
else:
    print("Andere Zahl")
```

## 🔍 Vergleichsoperatoren
- == gleich

- != ungleich

- <, >, <=, >=

## 🔗 Boolesche Logik
- and → beide Bedingungen wahr

- or → mindestens eine Bedingung wahr

- not → Negation

## ⚠️ Fehlerquellen
- if x = 5: ❌ → SyntaxError (Zuweisung statt Vergleich)

- Einrückung nicht korrekt → IndentationError