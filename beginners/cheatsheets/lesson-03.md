# Cheatsheet – Lesson 3: Daten in Worten

## 🔑 Strings
```python
first = "Fabio"
last = "Rempel"
```

## 🖊️ f-Strings
```python
print(f"Hallo {first} {last}")
```

## 🔧 String-Methoden

- .strip() → entfernt Leerzeichen am Anfang/Ende

- .lower() → alles klein

- .upper() → alles groß

- .title() → jedes Wort mit großem Anfangsbuchstaben

## 📝 Zeichen aus String
```python
name = "Fabio"
print(name[0])  # "F"
```
### ⚠️ Kein eigener "Char"-Typ – auch "F" ist ein String.

## ⚠️ Fehlerquellen
- IndexError: wenn man auf name[100] zugreift, das es nicht gibt
- .strip() entfernt keine Leerzeichen mitten im Text