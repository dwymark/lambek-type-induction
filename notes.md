<!-- This document is written in a format that is compatible with the "Markdown Math" plugin for vscode. -->
# Lambek Calculus

## Syntactic Rules

- **Rule 1**: "Simplification"
$$
(x/y)y \rightarrow x \\
y(y\backslash x) \rightarrow x
$$
- **Rule 2**: "V-Associativity"
$$
(x\backslash y)/z \leftrightarrows x\backslash (y/z)
$$
- **Rule 3**: "Elimination"
$$
(x/y)(y/z) \rightarrow x/z \\
(x\backslash y)(y\backslash z) \rightarrow x\backslash z
$$
- **Rule 4**: "Type Raising"
$$
x \rightarrow y/(x \backslash y) \\
x \rightarrow (y / x) \backslash x
$$

## Formal Type System

- Let $A$ and $B$ be expressions.
- Let $x \in type(A)$ and $y \in type(B)$.
  - Then $xy \in type(AB)$.
  - If $z \in type(AB)$, then $z/y \in type(A)$.
  - If $z \in type(AB)$, then $x\backslash z \in type(B)$.
- $x \rightarrow y \Leftrightarrow x \in type(A) \rightarrow y \in type(B)$
- $x \leftrightarrows y \Leftrightarrow x \rightarrow y \wedge y \rightarrow x$

## References
- "The Mathematics of Sentence Structure" by Joachim Lambek, 1958

