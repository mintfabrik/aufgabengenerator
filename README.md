# Mintfabrik Aufgabengenerator

## Installation

### Schritt 1: Anaconda installieren

1. Lade die passende Variante von [Anaconda](https://www.anaconda.com/download) für deinen Rechner herunter und installiere sie.
2. Starte nach der Installation die **Anaconda Prompt** (Windows) oder das **Terminal** (macOS/Linux).

### Schritt 2: Python-Umgebung für das Projekt erstellen

Erstelle eine separate Python-Umgebung für dieses Projekt:

```bash
# Neue Umgebung mit Python 3.12 erstellen
conda create -n aufgabengenerator python=3.12

# Umgebung aktivieren
conda activate aufgabengenerator
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
# Stelle sicher, dass die aufgabengenerator-Umgebung aktiv ist
conda activate aufgabengenerator

# Installiere die Abhängigkeiten
pip install -r requirements.txt
```

Die folgenden Pakete werden installiert:
- **sympy**: Für symbolische Mathematik
- **matplotlib**: Für das Erstellen von Diagrammen
- **sympy-plot-backends**: Für erweiterte Plotting-Funktionen

### Schritt 5: VS Code einrichten

1. Lade [VS Code](https://code.visualstudio.com/download) herunter und installiere es.

2. Installiere die **Python-Erweiterung** für VS Code:
   - Öffne VS Code
   - Gehe zu Erweiterungen (Strg+Shift+X)
   - Suche nach "Python" und installiere die offizielle Python-Erweiterung von Microsoft

3. Öffne das Projektverzeichnis in VS Code:
   ```bash
   code .
   ```
   (Führe diesen Befehl im Projektverzeichnis aus)

4. **Python-Interpreter auswählen**:
   - Drücke `Strg+Shift+P` (Windows/Linux) oder `Cmd+Shift+P` (macOS)
   - Gebe "Python: Select Interpreter" ein
   - Wähle den Interpreter aus der `aufgabengenerator`-Umgebung:
     - Windows: `~/anaconda3/envs/aufgabengenerator/python.exe`
     - macOS/Linux: `~/anaconda3/envs/aufgabengenerator/bin/python`

### Schritt 6: Installation testen

Teste, ob alles korrekt installiert ist:

```bash
# Stelle sicher, dass die aufgabengenerator-Umgebung aktiv ist
conda activate aufgabengenerator

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

**Problem: `conda` Befehl nicht gefunden**
- Starte die Anaconda Prompt neu oder füge Anaconda zu deinem PATH hinzu

**Problem: Falsche Python-Version**
- Überprüfe mit `python --version`, ob Python 3.12 verwendet wird
- Aktiviere die richtige Umgebung mit `conda activate aufgabengenerator`

**Problem: Module nicht gefunden**
- Stelle sicher, dass die `requirements.txt` installiert wurde: `pip install -r requirements.txt`
- Überprüfe, ob die richtige Python-Umgebung in VS Code ausgewählt ist

**Problem: VS Code erkennt die Anaconda-Umgebung nicht**
- Starte VS Code aus der Anaconda Prompt: `code .`
- Oder wähle manuell den Python-Interpreter über die Command Palette

## Eine Aufgabe erstellen

Erstelle im passenden Unterordner von `exercises` eine neue Funktion, die die Variablen `question` und `answer` zurückgibt.

## Varianten der Aufgabe erzeugen

Übergib deine Funktion an `Generating()` in `main.py` und rufe `main.py` mit deinem Python Interpreter auf.

## Erzeugte Varianten prüfen

Öffne die Datei `index.html` und prüfe, ob die gewünschten Varianten erstellt wurden.

