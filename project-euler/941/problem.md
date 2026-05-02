# Problem 941: de Bruijn's Combination Lock

de Bruijn has a digital combination lock with $k$ buttons numbered $0$ to $k-1$ where $k \\le 10$.  
The lock opens when the last $n$ buttons pressed match the preset combination.

Unfortunately he has forgotten the combination. He creates a sequence of these digits which contains every possible combination of length $n$. Then by pressing the buttons in this order he is sure to open the lock.

Consider all sequences of shortest possible length that contains every possible combination of the digits.  
Denote by $C(k, n)$ the lexicographically smallest of these.

For example, $C(3, 2) = $ 0010211220.

Define the sequence $a\_n$ by $a\_0=0$ and  
$$a\_n=(920461 a\_{n-1}+800217387569)\\bmod 10^{12} \\text{ for }\\ n > 0$$ Interpret each $a\_n$ as a $12$-digit combination, adding leading zeros for any $a\_n$ with less than $12$ digits.

Given a positive integer $N$, we are interested in the order the combinations $a\_1,\\dots,a\_N$ appear in $C(10,12)$.  
Denote by $p\_n$ the _place_, numbered $1,\\dots,N$, in which $a\_n$ appears out of $a\_1,\\dots,a\_N$. Define $\\displaystyle F(N)=\\sum\_{n=1}^Np\_na\_n$.

For example, the combination $a\_1=800217387569$ is entered before $a\_2=696996536878$. Therefore: $$F(2)=1\\cdot800217387569 + 2\\cdot696996536878 = 2194210461325$$ You are also given $F(10)=32698850376317$.

Find $F(10^7)$. Give your answer modulo $1234567891$.
