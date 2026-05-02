# Problem 652: Distinct Values of a Proto-logarithmic Function

Consider the values of $\\log\_2(8)$, $\\log\_4(64)$ and $\\log\_3(27)$. All three are equal to $3$.

Generally, the function $f(m,n)=\\log\_m(n)$ over integers $m,n \\ge 2$ has the property that  
$f(m\_1,n\_1)=f(m\_2,n\_2)$ if

1.  $\\, m\_1=a^e, n\_1=a^f, m\_2=b^e,n\_2=b^f \\,$ for some integers $a,b,e,f \\, \\,$ or
2.  $ \\, m\_1=a^e, n\_1=b^e, m\_2=a^f,n\_2=b^f \\,$ for some integers $a,b,e,f \\,$

We call a function $g(m,n)$ over integers $m,n \\ge 2$ proto-logarithmic if

-   $\\quad \\, \\, \\, \\, g(m\_1,n\_1)=g(m\_2,n\_2)$ if any integers $a,b,e,f$ fulfilling 1. or 2. can be found
-   **and** $\\, g(m\_1,n\_1) \\ne g(m\_2,n\_2)$ if no integers $a,b,e,f$ fulfilling 1. or 2. can be found.

Let $D(N)$ be the number of distinct values that any proto-logarithmic function $g(m,n)$ attains over $2\\le m, n\\le N$.  
For example, $D(5)=13$, $D(10)=69$, $D(100)=9607$ and $D(10000)=99959605$.

Find $D(10^{18})$, and give the last $9$ digits as answer.

  
**Note:** According to the **four exponentials conjecture** the function $\\log\_m(n)$ is proto-logarithmic.  
While this conjecture is yet unproven in general, $\\log\_m(n)$ can be used to calculate $D(N)$ for small values of $N$.
