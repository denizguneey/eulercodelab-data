# Problem 492: Exploding Sequence

Define the sequence $a\_1, a\_2, a\_3, \\dots$ as:

-   $a\_1 = 1$
-   $a\_{n+1} = 6a\_n^2 + 10a\_n + 3$ for $n \\ge 1$.

Examples:  
$a\_3 = 2359$  
$a\_6 = 269221280981320216750489044576319$  
$a\_6 \\bmod 1\\,000\\,000\\,007 = 203064689$  
$a\_{100} \\bmod 1\\,000\\,000\\,007 = 456482974$

Define $B(x,y,n)$ as $\\sum (a\_n \\bmod p)$ for every prime $p$ such that $x \\le p \\le x+y$.

Examples:  
$B(10^9, 10^3, 10^3) = 23674718882$  
$B(10^9, 10^3, 10^{15}) = 20731563854$

Find $B(10^9, 10^7, 10^{15})$.
