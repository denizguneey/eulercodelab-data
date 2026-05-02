# Problem 159: Digital Root Sums of Factorisations

A composite number can be factored many different ways. For instance, not including multiplication by one, $24$ can be factored in $7$ distinct ways:

$$\\begin{align} 24 &= 2 \\times 2 \\times 2 \\times 3\\\\ 24 &= 2 \\times 3 \\times 4\\\\ 24 &= 2 \\times 2 \\times 6\\\\ 24 &= 4 \\times 6\\\\ 24 &= 3 \\times 8\\\\ 24 &= 2 \\times 12\\\\ 24 &= 24 \\end{align}$$

Recall that the digital root of a number, in base $10$, is found by adding together the digits of that number, and repeating that process until a number is arrived at that is less than $10$. Thus the digital root of $467$ is $8$.

We shall call a Digital Root Sum (DRS) the sum of the digital roots of the individual factors of our number.  
The chart below demonstrates all of the DRS values for $24$.

<table class="grid center"><tbody><tr><th>Factorisation</th><th>Digital Root Sum</th></tr><tr><td>$2 \times 2 \times 2 \times 3$</td><td>$9$</td></tr><tr><td>$2 \times 3 \times 4$</td><td>$9$</td></tr><tr><td>$2 \times 2 \times 6$</td><td>$10$</td></tr><tr><td>$4 \times 6$</td><td>$10$</td></tr><tr><td>$3 \times 8$</td><td>$11$</td></tr><tr><td>$2 \times 12$</td><td>$5$</td></tr><tr><td>$24$</td><td>$6$</td></tr></tbody></table>

The maximum Digital Root Sum of $24$ is $11$.  
The function $\\operatorname{mdrs}(n)$ gives the maximum Digital Root Sum of $n$. So $\\operatorname{mdrs}(24)=11$.  
Find $\\sum \\operatorname{mdrs}(n)$ for $1 \\lt n \\lt 1\\,000\\,000$.
