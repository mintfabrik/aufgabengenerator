from random import choice

from spb import plot, MB
from sympy import symbols

from operations.plotting import mpl_axes, create_svg


def plot_template():
    #############################################################
    # Template für die Grafikerstellung
    #############################################################

    # BEISPIEL HYPERBEL-FUNKTION
    # Variablen und Parameter
    x = symbols('x',real=True)
    a = choice([-1,1])
    b = choice([-2,-1,0,0,1,2])
    n = choice([1,2])
    # Betragsfunktion g(x)
    g = a/(x+b)**n
    # Polstelle
    xpol = -b

    #############################################################

    # GRAFIK-TEIL
    # Limits
    X=5
    Y=5
    # Plots für einzelne Funktionen
    #fig, ax = plt.subplots()
    g_graph1 = plot(g, (x, -X, xpol-0.01), line_color="green", backend=MB)
    g_graph2 = plot(g, (x, xpol+0.01, X),  line_color="green", backend=MB)
    # Achsengrenzen einstellen
    ax = mpl_axes()
    ax.set_xlim(-X,X)
    ax.set_ylim(-X,X)


    #gwgraph = plot(gw, (x,-X,X), xlim=(-X,X), ylim=(-Y,Y), ax=mpl_axes(step=1, box_aspect=1, grid_lines='dotted', axis_arrows=True, xticks_off=False, yticks_off=False), xlabel='x', ylabel='g(x)', axis_center=(0,0), box = False, grid=False, backend=MB)


    # Beschriftungen verschieben
    #ax = plt.gca()
    #ax.set_xlabel("x", loc="right")
    #ax.set_ylabel("g(x)", loc="top")




    # Matplotlib Diagramm erzeugen
    #fig, ax = plt.subplots()
    # Grid-Einstellungen
    #ax.grid(linewidth=0.5, linestyle='--', color='gray')
    # Box an/aus
    #ax.spines['top'].set_visible(False)
    #ax.spines['right'].set_visible(False)
    # Position des Achsenursprungs
    #ax.spines['left'].set_position(('data', 0))
    #ax.spines['bottom'].set_position(('data', 0))
    # Achsenbeschriftungen
    #ax.set_xlabel('X-Achse')
    #ax.set_ylabel('Y-Achse')
    # Position der Achsenbeschriftungen
    #ax.xaxis.set_label_coords(1.05, -0.05)
    #ax.yaxis.set_label_coords(-0.05, 1.05)
    # Pfeilspitzen an den Achsen
    #ax.annotate('', xy=(1, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>'))
    #ax.annotate('', xy=(0, 1), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>'))
    # Legende an/aus
    #ax.plot([-X, xpol - 0.01], [g.subs(x, -X), g.subs(x, xpol - 0.01)], label='Kurve 1', color='green')
    #ax.plot([xpol + 0.01, X], [g.subs(x, xpol + 0.01), g.subs(x, X)], label='Kurve 2', color='green')
    #ax.legend()
    # Aspect Ratio einstellen
    #ax.set_aspect(1)
    # Markierungspunkt setzen
    #ax.scatter(1, g.subs(x, 1), color='red', s=100)
    # Pfeil zu einem Punkt setzen
    #ax.annotate('Wichtiger Punkt', xy=(1, g.subs(x, 1)), xytext=(2, g.subs(x, 1) + 1),
    #            arrowprops=dict(facecolor='blue', shrink=0.05))
    # Textfeld innerhalb der Grafik setzen
    #ax.text(0.5, g.subs(x, 2), 'Hier ist ein Textfeld', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))

    # Diagramm anzeigen
    #plt.show()

    # Kombiniere beide Plots
    g_graph1.extend(g_graph2)
    g_graph1.show()
    # Erzeuge svg
    g_svg = create_svg(g_graph1)
    # Frage und Antwort
    question = g_svg
    answer = "Das ist ein schönes Diagramm"
    return question, answer