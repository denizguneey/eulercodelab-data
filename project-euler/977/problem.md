# Problem 977: Iterated Functions

For a positive integer $n$, let $F(n)$ denote the number of functions $f$ from the set $S\_n=\\{1,2,\\dots,n\\}$ to itself such that $f^{(x)}(y)=f^{(y)}(x)$ for any $x,y$ in $S\_n$. Here $f^{(k)}$ denotes the $k$-th iterated composition of $f$, e.g. $f^{(2)}(x)=f(f(x))$.

For example, $F(3)=8$, $F(7)=174$, $F(100)=570271270297640131$.

Find $F(10^6) \\bmod (10^9+7)$.
