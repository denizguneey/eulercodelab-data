# Problem 732: Standing on the Shoulders of Trolls

$N$ trolls are in a hole that is $D\_N$ cm deep. The $n$-th troll is characterized by:

-   the distance from his feet to his shoulders in cm, $h\_n$
-   the length of his arms in cm, $l\_n$
-   his IQ (Irascibility Quotient), $q\_n$.

Trolls can pile up on top of each other, with each troll standing on the shoulders of the one below him. A troll can climb out of the hole and escape if his hands can reach to the surface. Once a troll escapes he cannot participate any further in the escaping effort.

The trolls execute an optimal strategy for maximizing the total IQ of the escaping trolls, defined as $Q(N)$.

Let  
$r\_n = \\left\[ \\left( 5^n \\bmod (10^9 + 7) \\right) \\bmod 101 \\right\] + 50$  
$h\_n = r\_{3n}$  
$l\_n = r\_{3n+1}$  
$q\_n = r\_{3n+2}$  
$D\_N = \\frac{1}{\\sqrt{2}} \\sum\_{n=0}^{N-1} h\_n$.

For example, the first troll ($n=0$) is 51cm tall to his shoulders, has 55cm long arms, and has an IQ of 75.

You are given that $Q(5) = 401$ and $Q(15)=941$.

Find $Q(1000)$.
