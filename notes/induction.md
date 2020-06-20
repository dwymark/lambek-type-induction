# Lambek Type Induction

This document explores the problem of type induction over a lambek calculus. The definitions and theorems from [Lambek Calculus Fundamentals](fundamentals.html) are referenced throughout.

## Problem Statement

Given a language $L=\{A\in X^+ : A\triangleright s\}$ and the set $X_P=\{A\in X : \exists p\in P,\ A\triangleright p\}$, determine a valid type assignment for $X$.

For the type assignment to be "interesting", it will be desirable to minimize the ambiguity of type assignments. In other words, the closer that $\triangleright$ is to a function rather than a relation, the better.

In order to better constrain the behavior of the type mapping, an optional set of negative examples $L^*\subseteq X^+ \setminus L$ can also be provided.

### Subproblems

- Does a valid type assignment always exist?
- How can we validate a type assignment? In other words, how do we parse a lexeme sequence where every lexeme has been assigned a type?

### Examples

...

## Existence Conditions

- The only edge case I can think of at this point is the one where all lexemes are assigned distinct primitive types. But even here, if we allow for ambiguity, we can come up with a type assignment.
  - Example:

    "My name is Daniel" $\triangleright\ a\cdot b\cdot c\cdot d$

    Even here, we can posit that "Daniel" is ambiguous, such that "Daniel" $\triangleright\ a\backslash(b\backslash(c\backslash s))$ also holds.


## Induction Procedure

- Rough first thought: do a greedy search for a valid type assignment, guided by the need to minimize type ambiguity.

## Validation Procedure

- Look into Pentus 1993, where it is proven that "lambek grammars are context free". Maybe you can derive a parsing mechanism from the work done in that paper.

## References

- Pentus, M. (1993, June). Lambek grammars are context free. In *[1993] Proceedings Eighth Annual IEEE Symposium on Logic in Computer Science* (pp. 429-433). IEEE.