from enum import Enum
from typing import List

from .type import Type
from .sequent import Sequent


_index_kind_strs = ["", "+", "*"]


class IndexKind(Enum):
    EXACTLY_ONE = 0
    ONE_OR_MORE = 1
    ZERO_OR_MORE = 2

    def __str__(self):
        return _index_kind_strs[self.value]  # pylint: disable=invalid-sequence-index


class Index(Type):
    def __init__(self, idx: int, kind: IndexKind):
        super().__init__()
        self.idx = idx
        self.kind = kind

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"${self.idx}{self.kind}"


class Rule:
    def __init__(self, premises: List[Sequent], conclusion: Sequent):
        self.premises = premises
        self.conclusion = conclusion

    def __repr__(self):
        return str(self)

    def __str__(self):
        lhs = "&".join([f"({t})" for t in self.premises])
        rhs = str(self.conclusion)
        return f"{lhs}=>({rhs})"

    def pretty_str(self):
        premises = [str(p) for p in self.premises]
        longest = max([len(p) for p in premises] + [len(str(self.conclusion))])
        return "\n".join(premises) + "\n" + "-" * longest + "\n" + str(self.conclusion)

    def pprint(self):
        print(self.pretty_str())

    @property
    def premises(self):
        return self._premises

    @premises.setter
    def premises(self, val):
        if not isinstance(val, list):
            val = [val]
        self._premises = val
