# Problem 992: Another Frog Jumping

There are $n+1$ stones in a pond, numbered $0$ to $n$.

A frog starts by jumping onto stone $0$. It then jumps between the stones, only ever jumping to adjacent ones. For fixed $k$, it makes exactly $k+i$ visits to each stone $i$ for $0 \\le i \\lt n$; however, there are no restrictions on the number of times stone $n$ is visited. The frog can finish on any stone.

If $n=3$ and $k=2$ it would visit stone $0$ two times, stone $1$ three times and stone $2$ four times.  
One way of achieving this is:  
$0 \\to 1 \\to 0 \\to 1 \\to 2 \\to 3 \\to 2 \\to 1 \\to 2 \\to 3 \\to 2$.

Let $J(n,k)$ be the number of ways the frog can make such a journey. For example, $J(3,2) = 17$, $J(6,1) = 1320$ and $J(6,5) = 16793280$.

Find $\\displaystyle \\sum\_{s=0}^4 J(500,10^s)$. Give your answer modulo $987898789$.
