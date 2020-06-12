# Lambek Calculus

In this document, I attempt to formalize the framework presented in Lambek's 1958 "The Mathematics of Sentence Structure". This is done without much in the way of a literature review. Essentially, my goal here is to "fill in the gaps" where Lambek did not provide proofs or formal definitions.

I do, however, modestly extend the framework in my treatment below. My sense is that the value of the multiplication operator on types for linguistic modeling comes from its resemblence to a "merge" operation. This is why I choose to enforce a tight relationship between the product length of a type (i.e. how many times the $\cdot$ operator occurs in the type) and the concatenation length of an expression (i.e. how many lexemes are concatenated to form the expression).

I am not aware of any sources that model Lambek's original approach in exactly this way. What I have seen more often is a proof-theoretic approach that focuses on the properties of the type system in isolation. The approach I take below is to use set-theoretic definitions and axioms to define a type system coupled with a language.

## Formal Definition

### Definitions

#### Foundational Notions

1. Let $P$ be a non-empty set. Elements of $P$ are called *primitive types*.
2. Let $s\in P$ be called the "sentence type".
3. Let $T \supset P$. Elements of $T$ are called *types*, and they are either of the form $a$, $a/b$, $a\backslash b$, or $ab$ (or $\ a\cdot b$) where $a,b\in T$.
4. Let $\rightarrow$ and $\rightleftarrows$ be relations on $T$, i.e. subsets of $T\times T$.
5. Let $X$ be a set of strings, called the *lexicon*. Elements of $X$ are called *lexemes*.
6. Let $X^+$ be the collection of all finite, non-empty lexeme sequences.
7. For all $A,B\in X^+$, where $A=\langle A_0, \ldots, A_n \rangle$ and $B=\langle B_0, \ldots, B_m \rangle$, define the *concatenation* $AB$ as the sequence $\langle A_0, \ldots, A_n, B_0, \ldots, B_m \rangle$.
8. Let $\triangleright \subseteq X^+\times T$. When $A \triangleright x$, we say $x$ is a *type* of $A$.
9. Let $L = \{A \triangleright s : A\in X^+ \}$ be non-empty. $L$ is called the *language*. Elements of $L$ are called *sentences*.
10. Let **LC** = $\langle X, L, P, \triangleright \rangle$. We call **LC** a *lambek calculus*.

#### Length Function

It is convenient to have a notion of "product length", i.e. how many times does the $\cdot$ operator occur in a type, or how many lexemes are there in a sentence.

**Definition**. Let $\mathtt{len}: X^{+}\ \cup\ T \rightarrow \mathbb{N}$, where:
  - For all lexemes $W\in X$, define $\mathtt{len}(W) = 1$.
  - For all lexeme sequences $A, B\in X^+$, define $\mathtt{len}(AB) = \mathtt{len}(A) + \mathtt{len}(B)$.
  - For all types $x\in T$,
    - If $x=y\cdot z$ for some $y,z\in T$ then $\mathtt{len}(x) = \mathtt{len}(y) + \mathtt{len}(z)$;
    - Otherwise, $\mathtt{len}(x)=1$.

Note that this definition of $\mathtt{len}$ over types specifically applies to cases where the dot operator is at the highest precedence operator. For instance, $\mathtt{len}((x\cdot y)/z)$ is equal to 1, not 2.

**Theorem**: $\mathtt{len}$ is a well defined function.

<details><summary>Proof (INCOMPLETE)</summary>
<p>

   - First, need to establish that $\mathtt{len}$ is well defined on $X^+$.
     - For all $W\in X$, $\mathtt{len}(W)=1$ by definition, and hence is well defined.
     - Suppose $\mathtt{len}$ is well defined on all $X^i$ where $i\leq n$ for some $n\in\mathbb{N}$.
       - Consider $A\in X^{n+1}$. Note that $A=A_0A_1\ldots A_n$.
       - Choose $m\in\mathbb{N}$ such that $0<m\leq n$.
       - Then $A=(A_0\ldots A_m)(A_{m+1}\ldots A_n)$.
       - Note that $(A_0\ldots A_m)\in X^{m+1}$ and $(A_{m+1}\ldots A_n)\in X^{n-m}$.
       - By inductive hypothesis, $\mathtt{len}$ is well defined on $X^{m+1}$ and $X^{n-m}$.
       - Since $\mathtt{len}(A) = \mathtt{len}(A_0\ldots A_m) + \mathtt{len}(A_{m+1}\ldots A_n)$ by definition, see that $\mathtt{len}$ is well defined on $X^{n+1}$.
   - Then we need to establish the same for $T$.
     - Clearly true, lacking convenient notation for proof ...
</p>
</details>


### Axioms

#### (A) Arrow Axioms

1. $\forall x,y \in T : x \rightarrow y \Leftrightarrow \forall A \in X^+: A \triangleright x \Rightarrow A \triangleright y$
2. $\forall x,y \in T : x \rightleftarrows y \Leftrightarrow x\rightarrow y \ \& \ y \rightarrow x$


#### (T) Type Axioms

1. Every non-sentence primitive type is instantiated at least once in the lexicon.

   $\forall p\in P\ \exists W \in X: p\not=s \Rightarrow W\triangleright p$

2. Every lexeme has at least one type of length 1.

   $\forall W\in X\ \exists x\in T: \mathtt{len}(x)=1\ \&\ W\triangleright x$

#### (P) Product Axioms

1. Every lexeme sequence with a product type is a concatentation of two lexeme sequences.

   $\forall A\in X^+\ \forall x,y \in T: A\triangleright xy \Rightarrow ( \exists B,C\in X^+ : A=BC\ \&\ B\triangleright x \ \&\ C \triangleright y)$

2. Concatenating two lexeme sequences multiplies their types.

   $\forall A,B\in X^+: A\triangleright x\ \& \ B\triangleright y \Rightarrow AB \triangleright xy$

#### (S) Slash Axioms

1. $\forall A \in X^+\ \forall y, z \in T : A \triangleright z/y \Leftrightarrow (\forall B \in X^+: B \triangleright y \Rightarrow AB \triangleright z)$
2. $\forall B \in X^+\ \forall x, z \in T :  B \triangleright x\backslash z \Leftrightarrow (\forall A \in X^+: A \triangleright x \Rightarrow AB \triangleright z)$

### Theorems

#### (LL) Length Lemmas


1. Product typed lexeme sequences are never of length one. <!--Note, this can probably be strengthened to len(A)=n.-->

   $\forall A\in X^+\ \forall x,y \in T: A\triangleright xy \Rightarrow \mathtt{len}(A)>1$

<details><summary>Proof</summary>
<p>

   - Assume $A\triangleright xy$.
   - Then by (P1), $A=BC$ for some $B,C\in X^+$ where $B\triangleright x$ and $C\triangleright y$.
   - Hence $\mathtt{len}(A) = \mathtt{len}(B) + \mathtt{len}(C) \geq 2$.
</p>
</details>

1. All lexeme sequences of length $n$ have a type of length $n$.

   $\forall A\in X^+: \mathtt{len}(A)=n \Rightarrow \exists x\in T : \mathtt{len}(x)=n\ \&\ A\triangleright x$

<details><summary>Proof</summary>
<p>

   - Proof by induction on length.
   - Assume $\mathtt{len}(A)=1$.
     - Then $A\in X$ by definition of $\mathtt{len}$.
     - Hence by (T2), $A\triangleright x$ for some $x\in T$ where $\mathtt{len}(x)=1$.
   - Assume the theorem is true for $\mathtt{len}(A) = n$.
     - Let $A\in X^T$ be such that $\mathtt{len}(A)=n+1$.
     - Hence $A=A_0\cdots A_n=(A_0\cdots A_{n-1})\cdot A_n$.
     - By inductive hypothesis, $(A_0\cdots A_{n-1}) \triangleright x$ for some $x\in T$ such that $\mathtt{len}(x)=n$.
     - By (T2), $A_n \triangleright y$ for some $y\in T$ where $\mathtt{len}(x)=1$.
     - Hence $A=(A_0\cdots A_{n-1})\cdot A_n\triangleright xy$ by (P2).
     - By definition, $\mathtt{len}(xy)=\mathtt{len}(x)+\mathtt{len}(y)=n+1$.
</p>
</details>

3. All lexeme sequences have at least one type.

   $\forall A \in X^+\ \exists x \in T: A \triangleright x$.

<details><summary>Proof</summary>
<p>

   - Follows immediately from (LL2).
</p>
</details>


#### (B) Lambek's Basic Theorems

1. $\forall x \in T: x \rightarrow x$

<details><summary>Proof</summary>
<p>

   - Note that, by (A1), $x \rightarrow x \Leftrightarrow \forall A \in L: A \triangleright x \Rightarrow A \triangleright x$.
   - This is true since $p\Rightarrow p$ is true for any proposition $p$.
</p>
</details>

2. $\forall x, y, z \in T: x(yz) \rightleftarrows (xy)z$

<details><summary>Proof</summary>
<p>

   - $\rightarrow$
     - By (A1), $x(yz) \rightarrow (xy)z$ if and only if $\forall A \in L: A \triangleright x(yz) \Rightarrow A \triangleright (xy)z$.
     - Suppose $A \triangleright x(yz)$. Then by (P1), $A=BC$ for some $B,C$ where $B\triangleright x$ and $C \triangleright yz$.
     - Again by (P1), get that $C=DE$ for some $D,E$ where $D\triangleright y$ and $E \triangleright z$.
     - Since $C=DE$ and $C\triangleright yz$, conclude $DE\triangleright yz$.
     - By (P2), conclude that $D\triangleright y$ and $E\triangleright z$.
     - $A = BDE$ has been established. Since concatenation is associative, $BDE = B(DE)$.
     - Since $A \triangleright x(yz)$, conclude $B(DE) \triangleright x(yz)$. By (P2), $B \triangleright x$.
     - Since $B \triangleright x$ and $D \triangleright y$, conclude $BD\triangleright xy$ by (P2).
     - Again by (P2), conclude $(BD)E \triangleright (xy)z$.
     - Since $A=B(DE)=(BD)E$, conclude $A\triangleright (xy)z$.
   - $\leftarrow$.
     - By (A1), $(xy)z \rightarrow x(yz)$ if and only if $\forall A \in L: A \triangleright (xy)z \Rightarrow A \triangleright x(yz)$.
     - Suppose $A \triangleright (xy)z$. Then by (P1), $A=BC$ for some $B,C$ where $B\triangleright (xy)$ and $C \triangleright z$.
     - Again by (P1), get that $B=DE$ for some $D,E$ where $D\triangleright x$ and $E \triangleright y$.
     - Since $B=DE$ and $B\triangleright xy$, conclude $DE\triangleright xy$.
     - By (P2), conclude that $D\triangleright x$ and $E\triangleright y$.
     - $A = DEC$ has been established. Since concatenation is associative, $DEC = (DE)C$.
     - Since $A \triangleright (xy)z$, conclude $(DE)C \triangleright (xy)z$. By (P2), $C \triangleright z$.
     - Since $E \triangleright y$ and $C \triangleright z$, conclude $EC\triangleright yz$ by (P2).
     - Again by (P2), conclude $D(EC) \triangleright x(yz)$.
     - Since $A=(DE)C=D(EC)$, conclude $A\triangleright x(yz)$.
</p>
</details>

1. $\forall x, y, z \in T: xy \rightarrow z \Leftrightarrow x \rightarrow z/y$

<details><summary>Proof</summary>
<p>

  - $\Rightarrow$
    - Assume $xy \rightarrow z$.
    - Let $A\triangleright x$ and $B\triangleright y$.
    - Then $AB\triangleright xy$ by (P2).
    - Hence $AB\triangleright z$ by (A1).
    - Since $B\triangleright y$ and $AB\triangleright z$, conclude $A\triangleright z/y$ by (S1).
    - Hence $x\rightarrow z/y$.
  - $\Leftarrow$
    - Assume $x\rightarrow z/y$.
    - Let $A\triangleright xy$.
    - By (P1), $A=BC$ for some $B,C$ such that $B\triangleright x$ and $C\triangleright y$.
    - Since $x\rightarrow z/y$, conclude $B\triangleright z/y$ by (A1).
    - Since $B\triangleright z/y$ and $C\triangleright y$, conclude $BC\triangleright z$ by (S1).
    - Since $A=BC$, conclude $A\triangleright z$.
    - Hence $xy\rightarrow z$.
</p>
</details>

4. $\forall x, y \in T: xy \rightarrow z \Leftrightarrow y \rightarrow x\backslash z$

<details><summary>Proof</summary>
<p>

  - $\Rightarrow$
    - Assume $xy \rightarrow z$.
    - Let $A\triangleright x$ and $B\triangleright y$.
    - Then $AB\triangleright xy$ by (P2).
    - Hence $AB\triangleright z$ by (A1).
    - Since $A\triangleright x$ and $AB\triangleright z$, conclude $B\triangleright x\backslash z$ by (S2).
    - Hence $y\rightarrow x\backslash z$.
  - $\Leftarrow$
    - Assume $y\rightarrow x\backslash z$.
    - Let $A\triangleright xy$.
    - By (P1), $A=BC$ for some $B,C$ such that $B\triangleright x$ and $C\triangleright y$.
    - Since $x\rightarrow x\backslash z$, conclude $C\triangleright x\backslash z$ by (A1).
    - Since $C\triangleright x\backslash z$ and $B\triangleright x$, conclude $BC\triangleright z$ by (S2).
    - Since $A=BC$, conclude $A\triangleright z$.
    - Hence $xy\rightarrow z$.
</p>
</details>

1. $\forall x, y \in T: x\rightarrow y \ \&\ y\rightarrow z \Rightarrow x \rightarrow z$

<details><summary>Proof</summary>
<p>

   - Assume $x\rightarrow y$ and $y\rightarrow z$.
   - Let $A\triangleright x$.
   - Conclude $A\triangleright y$ by (A1).
   - Conclude $A\triangleright z$ by another application of (A1).
   - Hence $x\rightarrow z$.
</p>
</details>


## (X) Lambek's Extended Theorems

1. $(x/y)y \rightarrow x$

<details><summary>Proof</summary>
<p>

   - Assume $A\triangleright (x/y)y$.
   - By (P1), $A=BC$ where $B\triangleright x/y$ and $C\triangleright y$.
   - Hence by (S1), $BC\triangleright x$.
   - Hence $A\triangleright x$, proving $(x/y)y \rightarrow x$.
</p>
</details>


2. $y(y\backslash x) \rightarrow x$

<details><summary>Proof</summary>
<p>

   - Assume $A\triangleright y(y\backslash x)$.
   - By (P1), $A=BC$ where $B\triangleright y$ and $C\triangleright y\backslash x$.
   - Hence by (S2), $BC\triangleright y$.
   - Hence $A\triangleright y$, proving $y(y\backslash x) \rightarrow x$.
</p>
</details>

3.  $x\rightarrow x'\ \&\ y\rightarrow y' \Rightarrow xy\rightarrow x'y'$

<details><summary>Proof</summary>
<p>

  - Assume $x\rightarrow x'$ and $y\rightarrow y'$.
  - Assume $A\triangleright xy$.
  - Then $A=BC$ for some $B,C$ where $B\triangleright x$ and $C\triangleright y$ by (P1).
  - Hence $B\triangleright x'$ and $C\triangleright y'$ by (A1).
  - Hence $BC\triangleright x'y'$ by (P2).
  - Since $A=BC$, conclude $A\triangleright x'y'$.
  - Hence $xy\rightarrow x'y'$.
</p>
</details>


4. $x\rightarrow x'\ \&\ y\rightarrow y' \Rightarrow x/y'\rightarrow x'/y$
5. $x \rightarrow (xy)/y$

<details><summary>Proof</summary>
<p>

  - Note that $xy\rightarrow xy$ by (B1).
  - By (B3), conclude $x\rightarrow (xy)/y$.
</p>
</details>


1. $x\rightarrow (y/x)\backslash y$

<details><summary>Proof</summary>
<p>

  - Note that $(y/x)x \rightarrow y$ by (X1).
  - By (B4), conclude that $x \rightarrow (y/x)\backslash y$.
</p>
</details>


7. $x \rightarrow y/(x \backslash y)$
<details><summary>Proof</summary>
<p>

  - Note that $x(x\backslash y) \rightarrow y$ by (X2).
  - By (B3), conclude that $x \rightarrow y/(x \backslash y)$.
</p>
</details>

8. $(x/y)(y/z) \rightarrow x/z$
<details><summary>Proof</summary>
<p>

  - Note that $x/y \rightarrow x/y$ and $(y/z)z\rightarrow y$ by (B1) and (X1).
  - Hence $(x/y)(y/z)z\rightarrow (x/y)y$ by (X3).
  - Since $(x/y)y\rightarrow x$ by (X1) and $\rightarrow$ is transitive by (B5), conclude $(x/y)(y/z)z\rightarrow x$.
  - Hence $(x/y)(y/z)\rightarrow x/z$ by (B3).
</p>
</details>

9.  $(x\backslash y)(y\backslash z) \rightarrow x\backslash z$
<details><summary>Proof</summary>
<p>

  - Note that $x(x\backslash y)\rightarrow y$ and $y\backslash z\rightarrow y\backslash z$ by (X2) and (B1).
  - Hence $x(x\backslash y)(y\backslash z) \rightarrow y(y\backslash z)$ by (X3).
  - Since $y(y\backslash z) \rightarrow y$ by (X2) and $\rightarrow$ is transitive by (B5), conclude $x(x\backslash y)(y\backslash z)\rightarrow y$.
  - Hence $(x\backslash y)(y\backslash z)\rightarrow x\backslash z$ by (B4).
</p>
</details>

10.    $z/y\rightarrow (z/x)/(y/x)$
11.    $(x\backslash y)/z \rightleftarrows x\backslash (y/z)$
12.    $(x/y)/x\rightleftarrows x/(zy)$



## Miscellaneous Notes

1. By (LL2), all lexeme sequences of length $n$ have a type of length $n$. It does not appear to be the case that all types of length $n$ which are instantiated are necessarily instantiated by some expression of length $n$. I.e., seems you cannot prove that

   $\forall x\in T: \mathtt{len}(x)=n \ \&\ (\exists A\in X^+: A\triangleright x) \Rightarrow \exists A\in X^+ : \mathtt{len}(A)=n\ \&\ A\triangleright x$

## References
- "The Mathematics of Sentence Structure" by Joachim Lambek, 1958
