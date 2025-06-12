from typing import Callable

from generic_exercise_types import Exercises, Exercise
from utilities import clean


class CreateLoop:
    _max_runs = 1000
    _number_or_exercises = 50

    _runs = 0
    _results = 0
    _questions = set()


    def __init__(self):
        pass

    def run(self, generator: Callable):
        exercises: Exercises = []
        while self._runs < self._max_runs and self._results < self._number_or_exercises:
            self._runs += 1
            _question, _answer = generator()
            if clean(_question) in self._questions:
                continue
            self._questions.add(clean(_question))
            exercises.append(
                Exercise(question = clean(_question), answer = clean(_answer))
            )
            self._results += 1
        return exercises
