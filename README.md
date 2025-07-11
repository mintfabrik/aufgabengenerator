# Mintfabrik Aufgabengenerator

## Installation

### Schritt 1: Python installieren

1. Lade die neueste Python-Version von der [offiziellen Python-Website](https://www.python.org/downloads/) herunter:

![Python Download Page](https://github.com/user-attachments/assets/2b54e78b-56d8-464e-90a5-01851447d1c3)

**Betriebssystem-spezifische Installationshinweise:**

**Windows:**
- Lade die neueste Python-Version für Windows herunter
- **Wichtig:** Aktiviere beim Installer die Option "Add Python to PATH"
- Führe die Installation als Administrator aus

**macOS:**
- Lade die neueste Python-Version für macOS herunter
- Installiere die .pkg-Datei
- Alternativ: Verwende Homebrew: `brew install python`

**Linux (Ubuntu/Debian):**
```bash
# Aktualisiere die Paketliste
sudo apt update

# Installiere Python 3.12 und pip
sudo apt install python3.12 python3.12-venv python3.12-pip

# Setze Python 3.12 als Standard (optional)
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1
```

2. Überprüfe die Installation:
```bash
python --version
# oder auf manchen Systemen:
python3 --version
```

### Schritt 2: Virtuelle Python-Umgebung für das Projekt erstellen

Erstelle eine separate virtuelle Umgebung für dieses Projekt:

```bash
# Neue virtuelle Umgebung erstellen
python -m venv aufgabengenerator-env

# Umgebung aktivieren
# Windows:
aufgabengenerator-env\Scripts\activate

# macOS/Linux:
source aufgabengenerator-env/bin/activate
```

### Schritt 3: Projekt herunterladen

Lade das Projekt herunter oder klone es:

```bash
# Mit Git (falls installiert)
git clone https://github.com/mintfabrik/aufgabengenerator.git
cd aufgabengenerator

# Oder lade es als ZIP herunter und entpacke es
```

### Schritt 4: Abhängigkeiten installieren

Installiere die benötigten Python-Pakete aus der `requirements.txt`-Datei:

```bash
# Stelle sicher, dass die virtuelle Umgebung aktiv ist
# Windows:
aufgabengenerator-env\Scripts\activate
# macOS/Linux:
source aufgabengenerator-env/bin/activate

# Installiere die Abhängigkeiten
pip install -r requirements.txt
```

Die folgenden Pakete werden installiert:
- **sympy**: Für symbolische Mathematik
- **matplotlib**: Für das Erstellen von Diagrammen
- **sympy-plot-backends**: Für erweiterte Plotting-Funktionen

### Schritt 5: VS Code einrichten

1. **VS Code herunterladen und installieren:**

![Download Visual Studio Code](https://github.com/user-attachments/assets/1d435685-78ee-4226-a6c7-5ba115b84ccc)

   - Besuche [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
   - Wähle dein Betriebssystem (Windows, macOS oder Linux)
   - Lade den entsprechenden Installer herunter
   - Führe die Installation durch

2. **Python-Erweiterung installieren:**
   - Öffne VS Code
   - Klicke auf das Erweiterungen-Symbol in der Seitenleiste (oder drücke `Strg+Shift+X`)
   - Suche nach "Python"
   - Installiere die offizielle Python-Erweiterung von Microsoft
   - Starte VS Code neu, wenn erforderlich

3. **Projektverzeichnis in VS Code öffnen:**
   - Navigiere im Datei-Explorer zum `aufgabengenerator`-Ordner
   - Klicke mit der rechten Maustaste und wähle "Mit Code öffnen"
   - Oder öffne VS Code und verwende `Datei > Ordner öffnen...`

4. **VS Code Terminal öffnen:**
   - Drücke `Strg+Shift+ö` (Windows/Linux) oder `Cmd+Shift+ö` (macOS)
   - Oder gehe zu `Terminal > Neues Terminal` im Menü
   - Das Terminal sollte sich am unteren Bildschirmrand öffnen

5. **Virtuelle Umgebung im VS Code Terminal aktivieren:**
   
   Verwende ab sofort das VS Code Terminal für alle Kommandozeilen-Befehle:
   
   **Windows:**
   ```bash
   aufgabengenerator-env\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source aufgabengenerator-env/bin/activate
   ```
   
   Du solltest `(aufgabengenerator-env)` vor deiner Eingabeaufforderung sehen.

6. **Python-Interpreter auswählen:**
   - Drücke `Strg+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (macOS)
   - Gebe "Python: Select Interpreter" ein und wähle diesen Befehl
   - Wähle den Interpreter aus der `aufgabengenerator-env`-Umgebung:
     - Windows: `aufgabengenerator-env\Scripts\python.exe`
     - macOS/Linux: `aufgabengenerator-env/bin/python`
   - VS Code zeigt den ausgewählten Interpreter unten links in der Statusleiste an

### Schritt 6: Installation testen

Teste im VS Code Terminal, ob alles korrekt installiert ist:

```bash
# Stelle sicher, dass die virtuelle Umgebung aktiv ist (sollte bereits aktiv sein)
# Du solltest (aufgabengenerator-env) in der Eingabeaufforderung sehen

# Führe das Hauptprogramm aus
python main.py
```

Wenn alles funktioniert, solltest du die Meldung sehen:
```
Generated X exercises in X runs.
Created HTML file "index.html".
```

### Debugging in VS Code

Das Projekt ist bereits mit einer VS Code Debug-Konfiguration eingerichtet:

1. Öffne `main.py` in VS Code
2. Setze Breakpoints durch Klicken auf den linken Rand der Zeilennummern
3. Drücke `F5` oder gehe zu "Run and Debug" → "Python Debugger: main.py"

### Troubleshooting

**Problem: `python` Befehl nicht gefunden**
- Stelle sicher, dass Python korrekt installiert und zu deinem PATH hinzugefügt wurde
- Windows: Verwende möglicherweise `py` anstatt `python`
- Linux/macOS: Verwende möglicherweise `python3` anstatt `python`

**Problem: Virtuelle Umgebung kann nicht aktiviert werden**
- Windows: Überprüfe, ob PowerShell-Ausführungsrichtlinien korrekt gesetzt sind: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Stelle sicher, dass du dich im richtigen Verzeichnis befindest

**Problem: Falsche Python-Version**
- Überprüfe mit `python --version`, ob Python 3.12+ verwendet wird
- Aktiviere die virtuelle Umgebung korrekt

**Problem: Module nicht gefunden**
- Stelle sicher, dass die `requirements.txt` installiert wurde: `pip install -r requirements.txt`
- Überprüfe, ob die virtuelle Umgebung aktiviert ist
- Überprüfe, ob die richtige Python-Umgebung in VS Code ausgewählt ist

**Problem: VS Code erkennt die virtuelle Umgebung nicht**
- Stelle sicher, dass du den Python-Interpreter korrekt ausgewählt hast (siehe Schritt 5.6)
- Öffne ein neues VS Code Terminal (`Strg+Shift+ö`) und aktiviere die Umgebung manuell
- Oder wähle manuell den Python-Interpreter über die Command Palette (`Strg+Shift+P` → "Python: Select Interpreter")

## Eine Aufgabe erstellen

Erstelle im passenden Unterordner von `exercises` eine neue Funktion, die die Variablen `question` und `answer` zurückgibt.

## Varianten der Aufgabe erzeugen

Übergib deine Funktion an `Generating()` in `main.py` und rufe `main.py` mit deinem Python Interpreter auf.

## Erzeugte Varianten prüfen

Öffne die Datei `index.html` und prüfe, ob die gewünschten Varianten erstellt wurden.

