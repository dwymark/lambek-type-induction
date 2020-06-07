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

### Definitions

#### Foundational Sets and Relations

1. Let $X$ be a set of strings, called the *lexicon*. Elements of $X$ are called *lexemes*.
2. Let $X^{\infty}$ be the collection of all finite, non-empty sequences of elements from $X$.
3. Let $L\subseteq X^{\infty}$ be non-empty. $L$ is called the *language*. Elements of $L\setminus X$ are called *phrases*.
4. Let $P$ be a non-empty set.  Elements of $P$ are called *primitive types*.
5. Let $T \supset P$. Elements of $T$ are called *types*, and they are either of the form $a$, $a/b$, $a\backslash b$, or $ab$ (or $\ a\cdot b$) where $a,b\in T$.
6. Let $\triangleright \in L\times T$. When $p \triangleright t$, we say $t$ is a *type* of $p$. The following conditions apply to the $\triangleright$ relation:
   1. All phrases have at least one type: $\forall A \in L\ \exist x \in T: A \triangleright x$.
   2. Every primitive type is instantiated at least once: $\forall p\in P\ \exists A \in L: A\triangleright p$
7. Let **LC** = $\langle L, T, P, \triangleright \rangle$. We call **LC** a *lambek calculus*.

#### Arrow Relations
1. $\forall x,y \in T : x \rightarrow y \Leftrightarrow \forall A \in L: A \triangleright x \Rightarrow A \triangleright y$
2. $\forall x,y \in T : x \rightleftarrows y \Leftrightarrow x\rightarrow y \ \& \ y \rightarrow x$

#### Auxiliary Functions

It is convenient to have a notion of "product length", i.e. how many times does the $\cdot$ operator occur in a type, or how many lexemes are there in a phrase.

1. Let $\texttt{len}: L\ \dot\cup\ T \rightarrow \mathbb{N}$, where:
   1. For all lexemes $W\in X$, define $\texttt{len}(W) = 1$.
   2. For all expressions $A, B\in L$, define $\texttt{len}(AB) = \texttt{len}(A) + \texttt{len}(B)$.
   3. For all types $x\in T$,
      1. If $x=y\cdot z$ for some $y,z\in T$ then $\texttt{len}(x) = \texttt{len}(y) + \texttt{len}(z)$;
      2. Otherwise, $len(x)=1$.

**Proof** that $\texttt{len}$ is a well defined function:
- First, need to establish that $\texttt{len}$ is well defined on $L$.
  - For all $W\in X^1$, $\texttt{len}(W)=1$ by definition, and hence is well defined.
  - Suppose $\texttt{len}$ is well defined on all $X^i$ where $i\leq n$ for some $n\in\mathbb{N}$.
    - Consider $A\in X^{n+1}$. Note that $A=A_0A_1\ldots A_n$.
    - Choose $m\in\mathbb{N}$ such that $0<m<n$.
    - Then $A=(A_0\ldots A_m)(A_{m+1}\ldots A_n)$.
    - Note that $(A_0\ldots A_m)\in X^{m+1}$ and $(A_{m+1}\ldots A_n)\in X^{n-m}$.
    - By inductive hypothesis, $\texttt{len}$ is well defined on $X^{m+1}$ and $X^{n-m}$.
    - Since $\texttt{len}(A) = \texttt{len}(A_0\ldots A_m) + \texttt{len}(A_{m+1}\ldots A_n)$ by definition, see that $\texttt{len}$ is well defined on $X^{n+1}$.
- Then we need to establish the same for $T$.
  - Clearly true, lacking convenient notation for proof ...

### Axioms

#### (P) Product Axioms

For all expressions $A,B\in L$ and all types $x,y \in T$,

1. $A\triangleright xy \Rightarrow ( \exists C,D\in L : A=CD\ \&\ C\triangleright x \ \&\ D \triangleright y)$
2. $A \triangleright x\ \& \ B\triangleright y \Rightarrow AB \triangleright xy$

For all lexemes $W\in X$,

3. $\exists x\in T: \texttt{len}(x)=1\ \&\ W\triangleright x$

#### (S) Slash Axioms

1. $\forall A \in L\ \forall y, z \in T : A \triangleright z/y \Leftrightarrow (\forall B \in L: B \triangleright y \Rightarrow AB \triangleright z)$
2. $\forall B \in L\ \forall x, z \in T :  B \triangleright x\backslash z \Leftrightarrow (\forall A \in L: A \triangleright x \Rightarrow AB \triangleright z)$

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
