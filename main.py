from create_loop import CreateLoop
from math.basics import punkt_strich
from rendering import Rendering

if __name__ == '__main__':
    loop = CreateLoop()
    exercises = loop.run(punkt_strich)
    render = Rendering('Test', 'Löse die Aufgabe', exercises)
    render.execute()