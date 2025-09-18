# Lesson 2 – Werte & Rechnen

Nachdem du in Lesson 1 dein erstes Skript geschrieben hast, lernst du hier,
wie du mit Variablen rechnest und Eingaben vom Benutzer verarbeitest.

---

## 🎯 Lernziele
- Variablen verstehen und nutzen
- Rechnen mit Operatoren
  - Grundrechenarten: `+`, `-`, `*`, `/`
  - Ganzzahl-Division: `//`
  - Rest: `%`
- Eingaben mit `input()` einlesen
- Datentypen umwandeln (`int`, `float`, `str`)
- Erste Fehler kennenlernen (`ValueError`)

---

## 📂 Inhalt dieser Lektion
- **starter/** – Codegerüst mit Variablen und Eingaben
- **final/** – Trinkgeldrechner und Einheitenumrechner

---

## 📝 Mini-Challenges
1. Schreibe ein Programm, das Trinkgeld mit 15% berechnet.  
2. Temperaturumrechner: Celsius in Fahrenheit (`°F = °C * 1.8 + 32`).  
3. Probiere absichtlich eine falsche Eingabe bei `int(input(...))` aus und beobachte den `ValueError`.  
   Schreibe dir eine kurze Notiz, warum der Fehler passiert.  

---

## ⚠️ Häufige Stolpersteine
- `=` ist Zuweisung, `==` ist Vergleich  
- `input()` liefert immer einen String → Umwandlung nötig für Rechnungen  
- Falsche Eingabe (z. B. Buchstaben statt Zahl) → `ValueError`  
- Bei Geldbeträgen lohnt es sich, Ergebnisse mit `round(..., 2)` auf 2 Nachkommastellen zu runden  
- Umrechnungsfaktoren können als **Konstanten** gespeichert werden, z. B. `KM_TO_MILES = 0.621371`
