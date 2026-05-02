# Problem 637: Flexible Digit Sum

Given any positive integer $n$, we can construct a new integer by inserting plus signs between some of the digits of the base $B$ representation of $n$, and then carrying out the additions.

For example, from $n=123\_{10}$ ($n$ in base $10$) we can construct the four base $10$ integers $123\_{10}$, $1+23=24\_{10}$, $12+3=15\_{10}$ and $1+2+3=6\_{10}$.

Let $f(n,B)$ be the smallest number of steps needed to arrive at a single-digit number in base $B$. For example, $f(7,10)=0$ and $f(123,10)=1$.

Let $g(n,B\_1,B\_2)$ be the sum of the positive integers $i$ not exceeding $n$ such that $f(i,B\_1)=f(i,B\_2)$.

You are given $g(100,10,3)=3302$.

Find $g(10^7,10,3)$.
