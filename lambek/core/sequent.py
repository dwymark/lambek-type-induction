from typing import List

from .type import Type


class Sequent:
    def __init__(self, antecedent: List[Type], succedent: Type):
        self.antecedent = antecedent
        self.succedent = succedent

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.antecedent) + 1

    def __str__(self):
        antecedent = ";".join([str(t) for t in self.antecedent])
        succedent = str(self.succedent)
        return f"{antecedent} -> {succedent}"

    @property
    def antecedent(self):
        return self._antecedent

    @antecedent.setter
    def antecedent(self, val):
        if not isinstance(val, list):
            val = [val]
        self._antecedent = val
