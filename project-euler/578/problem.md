# Problem 578: Integers with Decreasing Prime Powers

Any positive integer can be written as a product of prime powers: $p\_1^{a\_1} \\times p\_2^{a\_2} \\times \\cdots \\times p\_k^{a\_k}$,  
where $p\_i$ are distinct prime integers, $a\_i \\gt 0$ and $p\_i \\lt p\_j$ if $i \\lt j$.

A decreasing prime power positive integer is one for which $a\_i \\ge a\_j$ if $i \\lt j$.  
For example, $1$, $2$, $15=3 \\times 5$, $360=2^3 \\times 3^2 \\times 5$ and $1000=2^3 \\times 5^3$ are decreasing prime power integers.

Let $C(n)$ be the count of decreasing prime power positive integers not exceeding $n$.  
$C(100) = 94$ since all positive integers not exceeding $100$ have decreasing prime powers except $18$, $50$, $54$, $75$, $90$ and $98$.  
You are given $C(10^6) = 922052$.

Find $C(10^{13})$.
