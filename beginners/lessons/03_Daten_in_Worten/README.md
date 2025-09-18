# Lesson 3 – Daten in Worten

Nachdem du Zahlen und Rechnen kennengelernt hast, geht es jetzt um Texte: **Strings**.

---

## 🎯 Lernziele
- Strings verstehen und verwenden
- f-Strings für Textformatierung nutzen
- Wichtige Methoden anwenden: `.strip()`, `.lower()`, `.upper()`, `.title()`
- Initialen aus Strings berechnen
- Verstehen: Es gibt keinen eigenen Datentyp „Char“ in Python

---

## 📂 Inhalt dieser Lektion
- **starter/** – Codegerüst mit TODOs
- **final/** – Begrüßungsformular und Initialen-Rechner

---

## 📝 Mini-Challenges
1. Frage den Nutzer nach Vor- und Nachnamen und gib eine Begrüßung aus, die sauber mit `.title()` formatiert ist.  
2. Schreibe ein Programm, das die Initialen des Nutzers berechnet und in Großbuchstaben ausgibt.  
3. Bonus: Lasse den Nutzer einen Satz eingeben und gib ihn komplett in Kleinbuchstaben zurück.

---

## ⚠️ Häufige Stolpersteine
- In Python gibt es **keinen Char** – ein einzelnes Zeichen ist einfach ein String mit Länge 1.  
- `strip()` entfernt nur Leerzeichen am Anfang/Ende, nicht in der Mitte.  
- Tipp: Bei Namen immer `.strip().title()` nutzen, um Eingabefehler zu korrigieren.
