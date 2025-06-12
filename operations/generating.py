from typing import Callable

from exercises.types import Exercises, Exercise
from utilities import clean


class Generating:
    _runs = 0
    _questions = set()


    def __init__(self, generator: Callable, number_of_exercises: int = 2, max_runs: int = 10):
        self.generator = generator
        self.number_of_exercises = number_of_exercises
        self.max_runs = max_runs

    def execute(self):
        exercises: Exercises = []
        while self._runs < self.max_runs and len(exercises) < self.number_of_exercises:
            self._runs += 1
            _question, _answer = self.generator()
            if clean(_question) in self._questions:
                continue
            self._questions.add(clean(_question))
            exercises.append(
                Exercise(question = clean(_question), answer = clean(_answer))
            )
        print(f"Generated {len(exercises)} exercises in {self._runs} runs.")
        return exercises
