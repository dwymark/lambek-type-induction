from functools import reduce
from typing import List


class Type:
    pass


class Primitive(Type):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name

    def __len__(self):
        return 1


class Residue(Type):
    def __init__(self, lhs: Type, rhs: Type):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.lhs == other.lhs and self.rhs == other.rhs

    def __len__(self):
        return len(self.lhs) + len(self.rhs)


class LeftResidue(Residue):
    def __str__(self):
        return f"({self.lhs}\\{self.rhs})"

    def __eq__(self, other):
        return isinstance(other, LeftResidue) and super().__eq__(other)


class RightResidue(Residue):
    def __str__(self):
        return f"({self.lhs}/{self.rhs})"

    def __eq__(self, other):
        return isinstance(other, RightResidue) and super().__eq__(other)


class Product(Type):
    def __init__(self, operands: List[Type]):
        if not isinstance(operands, list):
            operands = [operands]
        self.operands = operands

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "*".join([str(t) for t in self.operands])

    def __iter__(self):
        for operand in self.operands:
            yield operand

    def __eq__(self, other):
        if len(self.operands) != len(other.operands):
            return False

        equal = True
        for operand, other_operand in zip(self, other):
            equal = equal and operand == other_operand
        return equal

    def __len__(self):
        return reduce(lambda x, y: x + y, [len(t) for t in self.operands])


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


