# Lesson 10 – Module nutzen, Umgebungen verstehen

Python hat eine riesige Standardbibliothek mit vielen nützlichen Modulen.
Außerdem kannst du mit `pip` externe Pakete installieren – am besten in
einer virtuellen Umgebung.

---

## 🎯 Lernziele
- Module importieren und nutzen
- Standardbibliothek: `math`, `random`, `datetime`
- Externe Pakete mit `pip` installieren
- Virtuelle Umgebung anlegen und aktivieren
- Kleines Spiel mit `random` + Highscore-Datei

---

## 📂 Inhalt dieser Lektion
- **starter/** – Codegerüst mit TODOs
- **final/** – Zahlratespiel mit Highscore

---

## 📝 Mini-Challenges
1. Erweitere das Zahlratespiel: Schwierigkeitsgrad (1–10, 1–100, 1–1000).  
2. Baue eine Statistik ein: Anzahl der Spiele, bester Highscore.  
3. Bonus: Nutze `datetime`, um das Datum des letzten Highscores zu speichern.  

---

## ⚠️ Häufige Stolpersteine
- `import modulename` muss am Anfang der Datei stehen  
- Virtuelle Umgebung muss vor `pip install` aktiviert sein  
- Highscore-Datei fehlt beim ersten Start → `FileNotFoundError` → mit `try/except` abfangen
