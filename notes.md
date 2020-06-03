# Lambek Calculus

## Syntactic Rules

- **Rule 1**: "Simplification"
$$
(x/y)y \rightarrow x
$$
$$
y(y\backslash x) \rightarrow x
$$

- **Rule 2**: "V-Associativity"
$$
(x\backslash y)/z \leftrightarrows x\backslash (y/z)
$$

- **Rule 3**: "Elimination"
$$
(x/y)(y/z) \rightarrow x/z
$$
$$
(x\backslash y)(y\backslash z) \rightarrow x\backslash z
$$

- **Rule 4**: "Type Raising"
$$
x \rightarrow y/(x \backslash y)
$$
$$
x \rightarrow (y / x) \backslash x
$$

## Formal Definition

### A. Definitions

1. Let $X$ be a set of strings, called the *lexicon*. Elements of $X$ are called *lexemes*.
2. Let $X^{\infty}$ be the collection of all finite, non-empty sequences of elements from $X$.
3. Let $L\subseteq X^{\infty}$ be non-empty. $L$ is called the *language*.
4. Let $P$ be a non-empty set.  Elements of $P$ are called *primitive types*.
5. Let $T \supset P$. Elements of $T$ are called *types*, and they are either of the form $a$, $a/b$, $a\backslash b$, or $ab$ (or $\ a\cdot b$) where $a,b\in T$.
6. Let $\triangleright \in L\times T$ be such that $\forall p \in L \exist t \in T: p \triangleright t$. When $p \triangleright t$, we say $t$ is a *type* of $p$.
7. Let **LC** = $\langle L, T, P, \triangleright \rangle$. We call **LC** a *lambek calculus*.

### B. Axioms

1. $\forall A\in L\ \forall x,y \in T : A\triangleright xy \Rightarrow ( \exists B,C\in L : A=BC\ \&\ B\triangleright x \ \&\ C \triangleright y)$
2. $\forall A, B \in L\ \forall x, y \in T : A \triangleright x\ \& \ B\triangleright y \Leftrightarrow AB \triangleright xy$
3. $\forall A, B \in L : B \triangleright y\ \& \ AB \triangleright z \Rightarrow A \triangleright z/y$
4. $\forall A, B \in L : A \triangleright x\ \& \ AB \triangleright z \Rightarrow B \triangleright x\backslash z$
5. $\forall x,y \in T : x \rightarrow y \Leftrightarrow \forall A \in L: A \triangleright x \Rightarrow A \triangleright y$
6. $\forall x,y \in T : x \rightleftarrows y \Leftrightarrow x\rightarrow y \ \& \ y \rightarrow x$

### C. Theorems

1. $\forall x \in T: x \rightarrow x$
  - **Proof**. Note that, by (B5), $x \rightarrow x \Leftrightarrow \forall A \in L: A \triangleright x \Rightarrow A \triangleright x$.
  - This is true since $p\Rightarrow p$ is true for any proposition $p$.

2. $\forall x, y, z \in T: x(yz) \rightleftarrows (xy)z$
  - **Proof**. $(\rightarrow)$
    - By (B5), $x(yz) \rightarrow (xy)z$ if and only if $\forall A \in L: A \triangleright x(yz) \Rightarrow A \triangleright (xy)z$.
    - Suppose $A \triangleright x(yz)$. Then by (B1), $A=BC$ for some $B,C$ where $B\triangleright x$ and $C \triangleright yz$.
    - Again by (B1), get that $C=DE$ for some $D,E$ where $D\triangleright y$ and $E \triangleright z$.
    - Since $C=DE$ and $C\triangleright yz$, conclude $DE\triangleright yz$.
    - By (B2), conclude that $D\triangleright y$ and $E\triangleright z$.
    - $A = BDE$ has been established. Since concatenation is associative, $BDE = B(DE)$.
    - Since $A \triangleright x(yz)$, conclude $B(DE) \triangleright x(yz)$. By (B2), $B \triangleright x$.
    - Since $B \triangleright x$ and $D \triangleright y$, conclude $BD\triangleright xy$ by (B2).
    - Again by (B2), conclude $(BD)E \triangleright (xy)z$.
    - Since $A=B(DE)=(BD)E$, conclude $A\triangleright (xy)z$.
  - Now we prove ($\leftarrow$).
    - By (B5), $(xy)z \rightarrow x(yz)$ if and only if $\forall A \in L: A \triangleright (xy)z \Rightarrow A \triangleright x(yz)$.
    - Suppose $A \triangleright (xy)z$. Then by (B1), $A=BC$ for some $B,C$ where $B\triangleright (xy)$ and $C \triangleright z$.
    - Again by (B1), get that $B=DE$ for some $D,E$ where $D\triangleright x$ and $E \triangleright y$.
    - Since $B=DE$ and $B\triangleright xy$, conclude $DE\triangleright xy$.
    - By (B2), conclude that $D\triangleright x$ and $E\triangleright y$.
    - $A = DEC$ has been established. Since concatenation is associative, $DEC = (DE)C$.
    - Since $A \triangleright (xy)z$, conclude $(DE)C \triangleright (xy)z$. By (B2), $C \triangleright z$.
    - Since $E \triangleright y$ and $C \triangleright z$, conclude $EC\triangleright yz$ by (B2).
    - Again by (B2), conclude $D(EC) \triangleright x(yz)$.
    - Since $A=(DE)C=D(EC)$, conclude $A\triangleright x(yz)$.

3. $\forall x, y \in T: xy \rightarrow z \Leftrightarrow x \rightarrow z/y$
  - **Proof**. $(\Rightarrow)$
    - Assume $xy \rightarrow z$.
    - Assume $A \triangleright xy$. Then by (B1), $A=BC$ for some $B,C$ where $B \triangleright x$ and $B \triangleright y$.
    - Since $BC \triangleright xy$ and $xy \rightarrow z$, by (B5) conclude $BC \triangleright z$.
    - Since $C \triangleright y$ and $BC \triangleright z$, by (B3) conclude $B\triangleright z/y$.
    - ...?
  - Now we prove ($\Leftarrow$).
    - stub
4. $\forall x, y \in T: xy \rightarrow z \Leftrightarrow y \rightarrow x\backslash y$
  - **Proof**.
    - stub

5. $\forall x, y \in T: x\rightarrow y \ \&\ y\rightarrow z \Rightarrow x \rightarrow z$
  - **Proof**.
    - stub


## References
- "The Mathematics of Sentence Structure" by Joachim Lambek, 1958
