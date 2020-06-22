import logging
import unittest

from lambek.core.parse import try_parse
from lambek.core.type import Primitive, LeftResidue, RightResidue, Product


class ParseTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_primitive(self):
        # A string is a valid primitive iff it is a valid C variable name
        a = "a"
        b = "Hello"
        c = "FOO_1"
        d = "1a"
        e = "foo!"
        f = "foo bar"

        valid_a = try_parse(a)
        valid_b = try_parse(b)
        valid_c = try_parse(c)
        self.assertIsInstance(valid_a, Primitive)
        self.assertIsInstance(valid_b, Primitive)
        self.assertIsInstance(valid_c, Primitive)

        invalid_d = try_parse(d)
        invalid_e = try_parse(e)
        invalid_f = try_parse(f)
        self.assertIs(invalid_d, None)
        self.assertIs(invalid_e, None)
        self.assertIs(invalid_f, None)

        self.assertEqual(valid_a.name, a)
        self.assertEqual(valid_b.name, b)
        self.assertEqual(valid_c.name, c)

    def test_compound(self):
        self.assertIsInstance(try_parse(r"a/b"), RightResidue)
        self.assertIsInstance(try_parse(r"a\b"), LeftResidue)

        self.assertIs(try_parse(r"a/b/c"), None)
        self.assertIs(try_parse(r"a\b\c"), None)
        self.assertIsNot(try_parse(r"a\b/c"), None)

        self.assertEqual(str(try_parse(r"(a/b)/c")), r"((a/b)/c)")
        self.assertEqual(str(try_parse(r"a/(b/c)")), r"(a/(b/c))")
        self.assertEqual(str(try_parse(r"(a/(b/c))")), r"(a/(b/c))")

        self.assertEqual(str(try_parse(r"((a/(b/c))*(a/(b/c)))")), r"(a/(b/c))*(a/(b/c))")

