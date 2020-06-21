from typing import List

from .type import Type


class Sequent:
    def __init__(self, lhs: List[Type], rhs: Type):
        if not isinstance(lhs, list):
            lhs = [lhs]
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return str(self)

    def __str__(self):
        lhs = ";".join([str(t) for t in self.lhs])
        rhs = str(self.rhs)
        return f"{lhs} => {rhs}"
