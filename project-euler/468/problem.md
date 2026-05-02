# Problem 468: Smooth Divisors of Binomial Coefficients

An integer is called **B\-smooth** if none of its prime factors is greater than $B$.

Let $S\_B(n)$ be the largest $B$-smooth divisor of $n$.  
Examples:  
$S\_1(10)=1$  
$S\_4(2100) = 12$  
$S\_{17}(2496144) = 5712$

Define $\\displaystyle F(n)=\\sum\_{B=1}^n \\sum\_{r=0}^n S\_B(\\binom n r)$. Here, $\\displaystyle \\binom n r$ denotes the binomial coefficient.  
Examples:  
$F(11) = 3132$  
$F(1111) \\mod 1\\,000\\,000\\,993 = 706036312$  
$F(111\\,111) \\mod 1\\,000\\,000\\,993 = 22156169$

Find $F(11\\,111\\,111) \\mod 1\\,000\\,000\\,993$.
