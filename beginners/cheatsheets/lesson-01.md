# Cheatsheet – Lesson 01

## 🚀 Erste Schritte mit Python
- Python-Skripte enden auf `.py`
- Ausführen im Terminal:
  - **Windows:** `python hello.py`
  - **Mac/Linux:** `python3 hello.py`
- Zwei Modi:
  - **REPL:** direkt interaktiv (`>>> 2+2`)
  - **Skript:** gespeicherte Datei (`.py`), beliebig oft ausführbar

---

## 🖨️ Ausgabe
```python
print("Hello World")
```

## 🗒️ Kommentare
- **Kommentare beginnen mit #**
```python
# Dies ist ein Kommentar
print("Hallo Welt")  # Kommentar hinter Code
```

## ⬅️ Einrückung
- **Python nutzt Einrückungen (Leerzeichen) für Blockstruktur**
```python
if True:
    print("Korrekt eingerückt")
```

## ❌ Fehler (unerwartete Einrückung):
```python
print("Hallo")
    print("Welt")
```

## ⚠️ Unterschiede je nach System
- **Windows: Befehl python**

- **Mac/Linux: Befehl python3**

## 🛑 Typische Stolpersteine
- **IndentationError:** Einrückung stimmt nicht
- **Encoding-Probleme:** Umlaute/Sonderzeichen können je nach System Probleme machen (Grüße → notfalls Gruesse)