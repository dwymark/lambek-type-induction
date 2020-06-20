import logging

from lark import Lark, Transformer, v_args

from .type import LeftResidue, Primitive, Product, RightResidue

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
    def build_primitive(self, name):
        return Primitive(name.value)

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
