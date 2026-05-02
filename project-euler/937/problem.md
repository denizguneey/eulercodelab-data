# Problem 937: Equiproduct Partition

Let $\\theta=\\sqrt{-2}$.

Define $T$ to be the set of numbers of the form $a+b\\theta$, where $a$ and $b$ are integers and either $a\\gt 0$, or $a=0$ and $b\\gt 0$. For a set $S \\subseteq T$ and element $z \\in T$, define $p(S,z)$ to be the number of ways of choosing two distinct elements from $S$ with product either $z$ or $-z$.

For example if $S=\\{1,2,4\\}$ and $z=4$, there is only one valid pair of elements with product $\\pm4$, namely $1$ and $4$. Thus, in this case $p(S,z)=1$.

For another example, if $S=\\{1,\\theta,1+\\theta,2-\\theta\\}$ and $z=2-\\theta$, we have $1\\cdot(2-\\theta)=z$ and $\\theta\\cdot(1+\\theta)=-z$, giving $p(S,z)=2$.

Let $A$ and $B$ be two sets satisfying the following conditions:

-   $1 \\in A$
-   $A \\cap B = \\emptyset$
-   $A \\cup B = T$
-   $p(A,z) = p(B,z)$ for all $z\\in T$

Remarkably, these four conditions uniquely determine the sets $A$ and $B$.

Let $F\_n$ be the set of the first $n$ factorials: $F\_n=\\{1!,2!,\\dots,n!\\}$, and define $G(n)$ to be the sum of all elements of $F\_n\\cap A$.

You are given $G(4) = 25$, $G(7) = 745$, and $G(100) \\equiv 709772949 \\pmod{10^9+7}$.

Find $G(10^8)$ and give your answer modulo $10^9+7$.
