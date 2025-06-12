from dataclasses import dataclass
from typing import List


@dataclass
class Exercise:
    question: str
    answer: str

Exercises = List[Exercise]