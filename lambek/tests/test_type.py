import logging
import unittest

from lambek.core.type import Primitive, LeftResidue, RightResidue, Product


class TypeTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)
        self.alb = LeftResidue(Primitive('a'), Primitive('b'))
        self.arb = RightResidue(Primitive('a'), Primitive('b'))
        self.bla = LeftResidue(Primitive('b'), Primitive('a'))
        self.bra = RightResidue(Primitive('b'), Primitive('a'))


    def test_primitive(self):
        names = ['a', 'a', 'A', 'b']
        prims = [Primitive(name) for name in names]

        for i, prim in enumerate(prims):
            self.assertEqual(prim.name, names[i])
            self.assertEqual(str(prim), names[i])

        # Names are case sensitive
        self.assertEqual(prims[0], prims[1])    # a == a
        self.assertNotEqual(prims[0], prims[2]) # a != A

    def test_compound_equality(self):
        alb_copy = LeftResidue(Primitive('a'), Primitive('b'))

        p1 = Product([self.alb]) # Shouldn't really ever have len 1,
        p2 = Product([alb_copy]) # but no need to enforce that.
        p3 = Product([self.alb, self.alb])
        p4 = Product([alb_copy, alb_copy])
        p5 = Product([self.arb, self.bra])
        p6 = Product([self.bra, self.bla])

        self.assertEqual(self.alb, self.alb)
        self.assertEqual(self.alb, alb_copy)
        self.assertNotEqual(self.alb, self.arb)
        self.assertNotEqual(self.arb, self.bla)
        self.assertNotEqual(self.bla, self.bra)
        self.assertNotEqual(self.bra, self.alb)

        self.assertEqual(p1, p1)
        self.assertEqual(p1, p2)
        self.assertEqual(p3, p3)
        self.assertEqual(p3, p4)
        self.assertNotEqual(p1, p3)
        self.assertNotEqual(p3, p5)
        self.assertNotEqual(p5, p6)

    def test_str(self):
        p1 = Product([self.arb, self.bra])
        embedded = LeftResidue(self.arb, self.alb)

        self.assertEqual(str(Primitive('a')), "a")
        self.assertEqual(str(self.arb), "(a/b)")
        self.assertEqual(str(self.bra), "(b/a)")
        self.assertEqual(str(p1), "(a/b)*(b/a)")
        self.assertEqual(str(embedded), r"((a/b)\(a\b))")

