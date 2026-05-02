# Problem 447: Retractions C

For every integer $n>1$, the family of functions $f\_{n,a,b}$ is defined by  
$f\_{n,a,b}(x)\\equiv a x + b \\mod n\\,\\,\\, $ for $a,b,x$ integer and $0< a <n, 0 \\le b < n,0 \\le x < n$.

We will call $f\_{n,a,b}$ a _retraction_ if $\\,\\,\\, f\_{n,a,b}(f\_{n,a,b}(x)) \\equiv f\_{n,a,b}(x) \\mod n \\,\\,\\,$ for every $0 \\le x < n$.  
Let $R(n)$ be the number of retractions for $n$.

$\\displaystyle F(N)=\\sum\_{n=2}^N R(n)$.  
$F(10^7)\\equiv 638042271 \\mod 1\\,000\\,000\\,007$.  

Find $F(10^{14})$.  
Give your answer modulo $1\\,000\\,000\\,007$.
