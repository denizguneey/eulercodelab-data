# Problem 517: A Real Recursion

For every real number $a \\gt 1$ is given the sequence $g\_a$ by:  
$g\_{a}(x)=1$ for $x \\lt a$  
$g\_{a}(x)=g\_{a}(x-1)+g\_a(x-a)$ for $x \\ge a$  
$G(n)=g\_{\\sqrt {n}}(n)$  
$G(90)=7564511$.

Find $\\sum G(p)$ for $p$ prime and $10000000 \\lt p \\lt 10010000$  
Give your answer modulo $1000000007$.
