# Problem 940: Two-Dimensional Recurrence

The **Fibonacci sequence** $(f\_i)$ is the unique sequence such that

-   $f\_0=0$
-   $f\_1=1$
-   $f\_{i+1}=f\_i+f\_{i-1}$

Similarly, there is a unique function $A(m,n)$ such that

-   $A(0,0)=0$
-   $A(0,1)=1$
-   $A(m+1,n)=A(m,n+1)+A(m,n)$
-   $A(m+1,n+1)=2A(m+1,n)+A(m,n)$

Define $S(k)=\\displaystyle\\sum\_{i=2}^k\\sum\_{j=2}^k A(f\_i,f\_j)$. For example $$ \\begin{align} S(3)&=A(1,1)+A(1,2)+A(2,1)+A(2,2)\\\\ &=2+5+7+16\\\\ &=30 \\end{align} $$You are also given $S(5)=10396$.

Find $S(50)$, giving your answer modulo $1123581313$.
