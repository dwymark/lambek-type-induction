import logging
import time
from typing import List

from lark import Lark, Transformer, v_args

# Logging config
# ----------------------------------------------------------------------
DEBUGGING = True
UNIQUE_FILE = False

_filename = "debug.log"
if UNIQUE_FILE:
    _filename = f"{str(int(time.time() * 10000))}_" + _filename

if DEBUGGING:
    logging.basicConfig(
        filename=_filename, level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        filename=_filename, level=logging.WARNING,
    )

# Parsing
# ----------------------------------------------------------------------
_type_grammar = r"""
    start: type -> pass_through

    type: PRIMITIVE    -> build_primitive
        | compound     -> pass_through
        | product      -> pass_through
        | "(" type ")" -> pass_through

    compound: compound_inner -> pass_through

    compound_inner: type OVER type            -> build_right_residue
                  | type UNDER type           -> build_left_residue
                  | type UNDER type OVER type -> build_vee

    product: product       TIMES type -> expand_product
           | product_inner TIMES type -> expand_product

    product_inner: type -> build_product

    OVER: "/"
    UNDER: /\\/
    TIMES: "*"

    %import common.CNAME -> PRIMITIVE
    %ignore " "
"""


@v_args(inline=True)
class TypeBuilder(Transformer):
    def build_primitive(self, name: str):
        return Primitive(name)

    def build_left_residue(self, type_a, _, type_b):
        return LeftResidue(type_a, type_b)

    def build_right_residue(self, type_a, _, type_b):
        return RightResidue(type_a, type_b)

    def expand_product(self, product, _, type_):
        product.operands.append(type_)
        return product

    def build_product(self, type_):
        return Product([type_])

    def pass_through(self, rhs):
        return rhs


_parser = Lark(_type_grammar)
_transformer = TypeBuilder()


def _parse(string):  # DEBUG
    return _parser.parse(string)


def try_parse(string):
    """Try to parse string as a lambek type.
    If the parse succeeds, return a Type.
    If the parse fails, return None.
    """
    try:
        tree = _parser.parse(string)
    except Exception:  # pylint: disable=broad-except
        logging.error("Lambek: Parsing failed for %s", string, exc_info=True)
        return None

    try:
        return _transformer.transform(tree)
    except Exception:  # pylint: disable=broad-except
        logging.error("Lambek: Transform failed for %s", string, exc_info=True)

    return None


# Lambek Types
# ----------------------------------------------------------------------
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

# Main
# ----------------------------------------------------------------------
if __name__ == "__main__":
    a = try_parse(r"(a/b)\c")
    b = try_parse(r"(a\b/c)/(a\b)")
    c = try_parse(r"(a/b)*b*c")
    d = try_parse(r"(a/b)*b*(c)")
