import logging
import unittest

from lambek.core.type import Primitive, LeftResidue, RightResidue, Product
from lambek.core.sequent import Sequent
from lambek.core.rule import Rule
from lambek.core.parse import try_parse as type_


class RuleTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_str(self):
        abba = Sequent([type_("a/b"), type_("b")], type_("a"))
        r = Rule([abba, abba], abba)
        self.assertEqual(str(r), "((a/b);b->a)&((a/b);b->a)=>((a/b);b->a)")

