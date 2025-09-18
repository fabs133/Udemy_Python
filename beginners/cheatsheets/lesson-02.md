# Cheatsheet – Lesson 2: Werte & Rechnen

## 🔑 Variablen & Zuweisung
```python
name = "Fabio"
age = 30
```

## ➕ Operatoren

- + Addition

- - Subtraktion

- * Multiplikation

- / Division (float)

- // Ganzzahldivision

- % Rest

## ⌨️ Eingaben
```python
value = input("Gib etwas ein: ")  # immer String
```

## 🔄 Typumwandlung
```python
num = int("42")    # String → Integer
pi  = float("3.14") # String → Float
text = str(123)    # Zahl → String
```

## ⚠️ Fehler

- ValueError: passiert, wenn Eingabe nicht in Zahl umgewandelt werden kann
```python
age = int("zwanzig")  # ❌ Fehler
```