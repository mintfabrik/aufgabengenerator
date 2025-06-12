from exercises.mathematics.functions import plot_template
from operations.generating import Generating
from exercises.mathematics.basics import punkt_strich
from operations.rendering import Rendering

if __name__ == '__main__':
    loop = Generating(punkt_strich, 5, 20)
    exercises = loop.execute()
    render = Rendering('Test', 'Löse die Aufgabe', exercises)
    render.execute()