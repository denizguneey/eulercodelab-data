# Problem 433: Steps in Euclid's Algorithm

Let $E(x\_0, y\_0)$ be the number of steps it takes to determine the greatest common divisor of $x\_0$ and $y\_0$ with **Euclid's algorithm**. More formally:  
$x\_1 = y\_0$, $y\_1 = x\_0 \\bmod y\_0$  
$x\_n = y\_{n-1}$, $y\_n = x\_{n-1} \\bmod y\_{n-1}$  
$E(x\_0, y\_0)$ is the smallest $n$ such that $y\_n = 0$.

We have $E(1,1) = 1$, $E(10,6) = 3$ and $E(6,10) = 4$.

Define $S(N)$ as the sum of $E(x,y)$ for $1 \\leq x,y \\leq N$.  
We have $S(1) = 1$, $S(10) = 221$ and $S(100) = 39826$.

Find $S(5\\cdot 10^6)$.
