# Problem 445: Retractions A

For every integer $n>1$, the family of functions $f\_{n,a,b}$ is defined by  
$f\_{n,a,b}(x)\\equiv a x + b \\mod n\\,\\,\\, $ for $a,b,x$ integer and $0< a <n, 0 \\le b < n,0 \\le x < n$.

We will call $f\_{n,a,b}$ a _retraction_ if $\\,\\,\\, f\_{n,a,b}(f\_{n,a,b}(x)) \\equiv f\_{n,a,b}(x) \\mod n \\,\\,\\,$ for every $0 \\le x < n$.  
Let $R(n)$ be the number of retractions for $n$.

You are given that  
$\\displaystyle \\sum\_{k=1}^{99\\,999} R(\\binom {100\\,000} k) \\equiv 628701600 \\mod 1\\,000\\,000\\,007$.

Find $\\displaystyle \\sum\_{k=1}^{9\\,999\\,999} R(\\binom {10\\,000\\,000} k)$.  
Give your answer modulo $1\\,000\\,000\\,007$.
