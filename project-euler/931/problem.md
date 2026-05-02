# Problem 931: Totient Graph

For a positive integer $n$ construct a graph using all the divisors of $n$ as the vertices. An edge is drawn between $a$ and $b$ if $a$ is divisible by $b$ and $a/b$ is prime, and is given weight $\\phi(a)-\\phi(b)$, where $\\phi$ is the Euler totient function.  
Define $t(n)$ to be the total weight of this graph.  
The example below shows that $t(45) = 52$

![0931\_totientgraph.png](./png/001.png)

Let $T(N)=\\displaystyle\\sum\_{n=1}^{N} t(n)$. You are given $T(10)=26$ and $T(10^2)=5282$.

Find $T(10^{12})$. Give your answer modulo $715827883$.
