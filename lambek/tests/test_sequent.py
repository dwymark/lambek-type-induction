import logging
import unittest

from lambek.core.type import Primitive, LeftResidue, RightResidue, Product
from lambek.core.sequent import Sequent


class SequentTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.alb = LeftResidue(Primitive("a"), Primitive("b"))
        self.arb = RightResidue(Primitive("a"), Primitive("b"))
        self.bla = LeftResidue(Primitive("b"), Primitive("a"))
        self.bra = RightResidue(Primitive("b"), Primitive("a"))

    def test_str(self):
        self.assertEqual(str(Sequent([self.arb], self.arb)), "(a/b) => (a/b)")
        self.assertEqual(
            str(Sequent([self.arb, Primitive("b")], Primitive("a"))), "(a/b);b => a"
        )
        self.assertEqual(
            str(Sequent(Product([self.arb, Primitive("b")]), Primitive("a"))),
            "(a/b)*b => a",
        )

    def test_len(self):
        s = Sequent(Primitive("a"), Primitive("a"))
        self.assertEqual(len(s), 2)

        s.antecedent = [self.arb, Primitive("b")]
        self.assertEqual(len(s), 3)

        s.succedent = self.bla
        self.assertEqual(len(s), 3)
