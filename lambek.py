import logging
from lark import Lark, Transformer, v_args

logging.basicConfig(level=logging.DEBUG)

_type_grammar = r"""
    start: type -> pass_through

    type: PRIMITIVE -> build_primitive
        | compound  -> pass_through

    compound: "(" compound_inner ")" -> pass_through
            | compound_inner         -> pass_through

    compound_inner: type OVER type            -> build_compound
                  | type UNDER type           -> build_compound
                  | type TIMES type           -> build_compound
                  | type UNDER type OVER type -> build_vee

    OVER: "/"
    UNDER: /\\/
    TIMES: "*"

    %import common.CNAME -> PRIMITIVE
    %ignore " "
"""


@v_args(inline=True)
class LambekTypeBuilder(Transformer):
    def build_primitive(self, name: str):
        return Primitive(name)

    def build_compound(self, type_a, operator, type_b):
        return Compound(operator, type_a, type_b)

    def build_vee(self, type_a, under, type_b, over, type_c):
        return Compound(over, Compound(under, type_a, type_b), type_c)

    def pass_through(self, rhs):
        return rhs


_parser = Lark(_type_grammar)
_transformer = LambekTypeBuilder()


def _parse(string):  # DEBUG
    return _parser.parse(string)


def try_parse(string):
    """Try to parse string as a lambek type.
    If the parse succeeds, return a LambekType.
    If the parse fails, return None.
    """
    try:
        tree = _parser.parse(string)
    except Exception:  # pylint: disable=broad-except
        logging.error("Lambek: Parsing failed for %s", string, exc_info=True)
        return None
    return _transformer.transform(tree)


class LambekType:
    pass


class Primitive(LambekType):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name


class Compound(LambekType):
    def __init__(self, operator, leftOperand, rightOperand):
        self.operator = operator
        self.leftOperand = leftOperand
        self.rightOperand = rightOperand

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"({self.leftOperand}{self.operator}{self.rightOperand})"


if __name__ == "__main__":
    a = try_parse(r"(a/b)\c")
    b = try_parse(r"(a\b/c)/(a\b)")
