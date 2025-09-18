# Lesson 9 – Dateien & einfache Datenformate

Programme können Daten dauerhaft speichern.  
Mit Dateien und JSON werden unsere Programme praktisch nutzbar.

---

## 🎯 Lernziele
- Dateien schreiben & lesen mit `with open`
- Dateipfade richtig angeben
- JSON als einfaches Datenformat nutzen (`json`-Modul)
- Aufgabenlisten speichern & laden

---

## 📂 Inhalt dieser Lektion
- **starter/** – Codegerüst mit TODOs
- **final/** – To-Do-Liste mit JSON-Speicherung

---

## 📝 Mini-Challenges
1. Erweitere die To-Do-Liste: Beim Start sollen bestehende Aufgaben aus der JSON-Datei geladen werden.  
2. Schreibe ein Kontaktbuch, das Namen & Telefonnummern als Dictionary speichert.  
3. Bonus: Speichere die Daten in einem Unterordner `data/` statt im Hauptverzeichnis.  

---

## ⚠️ Häufige Stolpersteine
- `"w"` überschreibt Dateien – mit `"a"` kannst du anhängen  
- Vergiss `with open(...):` nicht – sonst bleibt die Datei evtl. offen  
- JSON kann nur einfache Datentypen speichern (Strings, Zahlen, Listen, Dictionaries)  
- Pfade: lieber `/` statt `\` nutzen, dann läuft es auf allen Systemen
