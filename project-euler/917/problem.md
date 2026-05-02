# Problem 917: Minimal Path Using Additive Cost

The sequence $s\_n$ is defined by $s\_1 = 102022661$ and $s\_n = s\_{n-1}^2 \\bmod {998388889}$ for $n > 1$.

Let $a\_n = s\_{2n - 1}$ and $b\_n = s\_{2n}$ for $n=1,2,...$

Define an $N \\times N$ matrix whose values are $M\_{i,j} = a\_i + b\_j$.

Let $A(N)$ be the minimal path sum from $M\_{1,1}$ (top left) to $M\_{N,N}$ (bottom right), where each step is either right or down.

You are given $A(1) = 966774091$, $A(2) = 2388327490$ and $A(10) = 13389278727$.

Find $A(10^7)$.
