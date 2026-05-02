# Problem 635: Subset Sums

Let $A\_q(n)$ be the number of subsets, $B$, of the set $\\{1, 2, ..., q \\cdot n\\}$ that satisfy two conditions:  
1) $B$ has exactly $n$ elements;  
2) the sum of the elements of $B$ is divisible by $n$.

E.g. $A\_2(5)=52$ and $A\_3(5)=603$.

Let $S\_q(L)$ be $\\sum A\_q(p)$ where the sum is taken over all primes $p \\le L$.  
E.g. $S\_2(10)=554$, $S\_2(100)$ mod $1\\,000\\,000\\,009=100433628$ and  
$S\_3(100)$ mod $1\\,000\\,000\\,009=855618282$.

Find $S\_2(10^8)+S\_3(10^8)$. Give your answer modulo $1\\,000\\,000\\,009$.
