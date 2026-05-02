# Problem 915: Giant GCDs

The function $s(n)$ is defined recursively for positive integers by $s(1) = 1$ and $s(n+1) = \\big(s(n) - 1\\big)^3 +2$ for $n\\geq 1$.  
The sequence begins: $s(1) = 1, s(2) = 2, s(3) = 3, s(4) = 10, \\ldots$.

For positive integers $N$, define $$T(N) = \\sum\_{a=1}^N \\sum\_{b=1}^N \\gcd\\Big(s\\big(s(a)\\big), s\\big(s(b)\\big)\\Big).$$ You are given $T(3) = 12$, $T(4) \\equiv 24881925$ and $T(100)\\equiv 14416749$ both modulo $123456789$.

Find $T(10^8)$. Give your answer modulo $123456789$.
