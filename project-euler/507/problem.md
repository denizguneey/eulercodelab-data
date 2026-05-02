# Problem 507: Shortest Lattice Vector

Let $t\_n$ be the **tribonacci numbers** defined as:  
$t\_0 = t\_1 = 0$;  
$t\_2 = 1$;  
$t\_n = t\_{n-1} + t\_{n-2} + t\_{n-3}$ for $n \\ge 3$  
and let $r\_n = t\_n \\text{ mod } 10^7$.

For each pair of Vectors $V\_n=(v\_1,v\_2,v\_3)$ and $W\_n=(w\_1,w\_2,w\_3)$ with $v\_1=r\_{12n-11}-r\_{12n-10}, v\_2=r\_{12n-9}+r\_{12n-8}, v\_3=r\_{12n-7} \\cdot r\_{12n-6}$ and  
$w\_1=r\_{12n-5}-r\_{12n-4}, w\_2=r\_{12n-3}+r\_{12n-2}, w\_3=r\_{12n-1} \\cdot r\_{12n}$  
we define $S(n)$ as the minimal value of the manhattan length of the vector $D=k \\cdot V\_n+l \\cdot W\_n$ measured as $|k \\cdot v\_1+l \\cdot w\_1|+|k \\cdot v\_2+l \\cdot w\_2|+|k \\cdot v\_3+l \\cdot w\_3|$ for any integers $k$ and $l$ with $(k,l)\\neq (0,0)$.

The first vector pair is $(-1, 3, 28)$, $(-11, 125, 40826)$.  
You are given that $S(1)=32$ and $\\sum\_{n=1}^{10} S(n)=130762273722$.

Find $\\sum\_{n=1}^{20000000} S(n)$.
