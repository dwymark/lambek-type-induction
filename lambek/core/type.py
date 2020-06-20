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


class Residue(Type):
    def __init__(self, lhs: Type, rhs: Type):
        self.lhs = lhs
        self.rhs = rhs

    def __repr__(self):
        return str(self)


class LeftResidue(Residue):
    def __str__(self):
        return f"({self.lhs}\\{self.rhs})"


class RightResidue(Residue):
    def __str__(self):
        return f"({self.lhs}/{self.rhs})"


class Product(Type):
    def __init__(self, operands: List[Type]):
        self.operands = operands

    def __repr__(self):
        return str(self)

    def __str__(self):
        string = ""
        for operand in self.operands[:-1]:
            string += str(operand) + "*"
        string += str(self.operands[-1])
        return string


class Sequent:
    def __init__(self, lhs: List[Type], rhs: Type):
        pass
