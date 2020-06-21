import logging
import unittest

from lambek.core.parse import try_parse
from lambek.core.type import Primitive, LeftResidue, RightResidue, Product


class ParseTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_primitive(self):
        a = "a"
        b = "Hello"
        c = "FOO_1"
        d = "1a"
        e = "foo!"

        valid_a = try_parse(a)
        valid_b = try_parse(b)
        valid_c = try_parse(c)
        invalid_d = try_parse(d)
        invalid_e = try_parse(e)

        self.assertIsInstance(valid_a, Primitive)
        self.assertIsInstance(valid_b, Primitive)
        self.assertIsInstance(valid_c, Primitive)

        self.assertIs(invalid_d, None)
        self.assertIs(invalid_e, None)

        self.assertEqual(valid_a.name, a)
        self.assertEqual(valid_b.name, b)
        self.assertEqual(valid_c.name, c)

    def test_compound(self):
        a = r"a/b"
        b = r"a\b"
        c = r"a\b\c"

        valid_a = try_parse(a)
        valid_b = try_parse(b)

        self.assertIsInstance(valid_a, RightResidue)
        self.assertIsInstance(valid_b, LeftResidue)

        self.assertEqual(str(valid_a), "(a/b)")

        self.assertIs(try_parse(r"a/b/c"), None)
        self.assertIs(try_parse(r"a\b\c"), None)
        self.assertIsNot(try_parse(r"a\b/c"), None)

        self.assertEqual(str(try_parse(r"(a/b)/c")), r"((a/b)/c)")
        self.assertEqual(str(try_parse(r"a/(b/c)")), r"(a/(b/c))")
        self.assertEqual(str(try_parse(r"(a/(b/c))")), r"(a/(b/c))")

        self.assertEqual(str(try_parse(r"((a/(b/c))*(a/(b/c)))")), r"(a/(b/c))*(a/(b/c))")

