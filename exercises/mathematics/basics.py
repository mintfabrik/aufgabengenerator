from random import choice

from utilities import int_range

def punkt_strich():
    # Wähle Werte für die Variablen des Produkts
    p = choice(int_range(2,21))
    q = choice(int_range(2,21))
    # Wähle Werte für die Variablen der Summe
    a = choice(int_range(1,51))
    b = choice(int_range(1,51))

    # Berechne das Produkt und die Summe mit SymPy
    produkt = p*q
    summe = a+b

    # Erstelle die LaTeX-Anzeige der Fragen
    case1 = f"{p} \\cdot {q} = \\, ?"
    case2 = f"{produkt} : {p} = \\, ?"
    case3 = f"{a} + {b} = \\, ?"
    case4 = f"{summe} - {a} = \\, ?"

    # Wähle zufällig eine der vier Fragen aus
    V = choice(int_range(1,4))

    # Weise die Frage und die Antwort zu
    if V==1:
        question = case1
        answer = produkt
    elif V==2:
        question = case2
        answer = q
    elif V==3:
        question = case3
        answer = summe
    else:
        question = case4
        answer = b
    return question, answer