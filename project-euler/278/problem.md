# Problem 278: Linear Combinations of Semiprimes

Given the values of integers $1 < a\_1 < a\_2 < \\dots < a\_n$, consider the linear combination  
$q\_1 a\_1+q\_2 a\_2 + \\dots + q\_n a\_n=b$, using only integer values $q\_k \\ge 0$.

Note that for a given set of $a\_k$, it may be that not all values of $b$ are possible.  
For instance, if $a\_1=5$ and $a\_2=7$, there are no $q\_1 \\ge 0$ and $q\_2 \\ge 0$ such that $b$ could be  
$1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18$ or $23$.  
In fact, $23$ is the largest impossible value of $b$ for $a\_1=5$ and $a\_2=7$.  
We therefore call $f(5, 7) = 23$.  
Similarly, it can be shown that $f(6, 10, 15)=29$ and $f(14, 22, 77) = 195$.

Find $\\displaystyle \\sum f( p\\, q,p \\, r, q \\, r)$, where $p$, $q$ and $r$ are prime numbers and $p < q < r < 5000$.
