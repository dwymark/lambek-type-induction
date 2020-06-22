import logging
import unittest

from lambek.core.type import RightResidue
from lambek.core.sequent import Sequent
from lambek.core.rule import Rule, Index, IndexKind
from lambek.core.parse import try_parse as type_


class RuleTest(unittest.TestCase):
    def setUp(self):
        logging.disable(logging.CRITICAL)

    def test_str(self):
        abba = Sequent([type_("a/b"), type_("b")], type_("a"))
        r = Rule([abba, abba], abba)
        self.assertEqual(str(r), "((a/b);b->a)&((a/b);b->a)=>((a/b);b->a)")

    def test_index_str(self):
        a = Index(0, IndexKind.ONE_OR_MORE)
        b = Index(1, IndexKind.EXACTLY_ONE)
        s = Sequent(a, b)

        c = Index(2, IndexKind.ZERO_OR_MORE)
        d = Index(3, IndexKind.EXACTLY_ONE)
        e = Index(4, IndexKind.ZERO_OR_MORE)
        f = Index(5, IndexKind.EXACTLY_ONE)
        t = Sequent([c, d, e], f)

        u = Sequent([c, RightResidue(d, b), a, e], f)
        r = Rule([s, t], u)

        self.assertEqual(str(s), "$0+->$1")
        self.assertEqual(str(t), "$2*;$3;$4*->$5")
        self.assertEqual(str(u), "$2*;($3/$1);$0+;$4*->$5")
        self.assertEqual(
            str(r), "($0+->$1)&($2*;$3;$4*->$5)=>($2*;($3/$1);$0+;$4*->$5)"
        )
        self.assertEqual(
            r.pretty_str(),
            "$0+->$1\n$2*;$3;$4*->$5\n-----------------------\n$2*;($3/$1);$0+;$4*->$5",
        )
