# Problem 958: Euclid's Labour

The **Euclidean algorithm** can be used to find the **greatest common divisor** of two positive integers. At each step of the algorithm the smaller number is subtracted from the larger one. The algorithm terminates when the numbers are equal, which is then the greatest common divisor of the original numbers.

For two numbers $n$ and $m$, let $d(n, m)$ be the number of subtraction steps used by the Euclidean algorithm for computing the greatest common divisor of $n$ and $m$.

For a number $n$, let $f(n)$ be the positive number $m$ coprime to $n$ that minimizes $d(n, m)$. If more than one number attains the minimum, the minimal $m$ is chosen.

For example, at least four steps are needed for computing the GCD of $7$ and any positive number $m$ coprime to $7$. This number of steps is obtained by $m=2,3,4,5$, yielding $f(7)=2$. You are also given $f(89)=34$ and $f(8191) = 1856$.

Find $f(10^{12}+39)$.
