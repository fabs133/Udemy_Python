# Lesson 8 – Fehler verstehen & handhaben

Fehler sind in Python **Exceptions**. Sie stoppen das Programm – aber mit
`try` und `except` können wir sie abfangen und gezielt darauf reagieren.

---

## 🎯 Lernziele
- Exceptions lesen und verstehen
- Fehler mit `try/except` abfangen
- `else` und `finally` verwenden
- Defensive Programmierung: Programme absturzsicher machen
- Mindset: Fehler als Feedback, nicht als Urteil

---

## 📂 Inhalt dieser Lektion
- **starter/** – Codegerüst mit TODOs
- **final/** – Sichere Division und Eingabe-Schleife

---

## 📝 Mini-Challenges
1. Schreibe eine Funktion `get_int(prompt)`, die so lange nach Eingaben fragt, bis eine gültige Zahl eingegeben wird.  
2. Erweitere `safe_divide(a, b)`, sodass ein Hinweistext zurückgegeben wird, wenn b = 0 ist.  
3. Bonus: Baue in dein Zahlratespiel aus Lesson 5 ein `try/except` ein, damit falsche Eingaben das Spiel nicht abbrechen.

---

## ⚠️ Häufige Stolpersteine
- `except:` ohne Angabe fängt **alles** ab – besser gezielt z. B. `except ValueError:`  
- `finally` läuft immer, auch wenn ein Fehler auftritt  
- Rückgabe von Funktionen nicht vergessen (`return`)  
