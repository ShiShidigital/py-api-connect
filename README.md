# Inklu Connect Employer Jobsync Creator

Dieses Python-Skript ist ein einfaches Kommandozeilen-Tool zum Erstellen 
eines Employer Jobsync-Eintrags auf der Inklu Connect API. 
Es ermöglicht den Namen des Arbeitgebers in der Kommandozeile 
als Argument zu übergeben und den Jobsync-Eintrag zu erstellen.

## Installation

1. Voraussetzungen:
   - Python 3.x muss auf Ihrem System installiert sein.
   - Stellen Sie sicher, dass Python und die pip-Verwaltungswerkzeuge korrekt 
     installiert sind, um Pakete installieren zu können.

2. Installation des Requests-Moduls:
   Das Skript verwendet die requests-Bibliothek, um HTTP-Anfragen zu verarbeiten. 
   Pip sollte installiert sein:

   ```bash
   pip install requests
   ```

## Gebrauchsanweisung

1. Skript speichern:
   Speichere das Skript als _create_employer_jobsync.py_.

2. Als Kommandozeilen-Tool ausführen:
   Sie können das Skript mit dem Namen des Arbeitgebers als Argument über das Terminal ausführen:

   ```bash
   python create_employer_jobsync.py "Arbeitgeber Name"
   ```
   Ersetze "Arbeitgeber Name" durch den tatsächlichen Namen des gewünschten Arbeitgebers. An die Anführungszeichen denken!
   
3. Ausgabe:
   - Bei Erfolg wird eine Bestätigung zusammen mit der Antwort von Inklu Connect im JSON-Format ausgegeben.
   - Bei einem Fehler werden der HTTP-Statuscode und mögliche Fehlermeldungen angezeigt.