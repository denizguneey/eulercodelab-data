# Problem 833: Square Triangle Products

Triangle numbers $T\_k$ are integers of the form $\\frac{k(k+1)} 2$.  
A few triangle numbers happen to be perfect squares like $T\_1=1$ and $T\_8=36$, but more can be found when considering the product of two triangle numbers. For example, $T\_2 \\cdot T\_{24}=3 \\cdot 300=30^2$.

Let $S(n)$ be the sum of $c$ for all integers triples $(a, b, c)$ with $0<c \\le n$, $c^2=T\_a \\cdot T\_b$ and $0<a<b$. For example, $S(100)= \\sqrt{T\_1 T\_8}+\\sqrt{T\_2 T\_{24}}+\\sqrt{T\_1 T\_{49}}+\\sqrt{T\_3 T\_{48}}=6+30+35+84=155$.

You are given $S(10^5)=1479802$ and $S(10^9)=241614948794$.

Find $S(10^{35})$. Give your answer modulo $136101521$.
