# Problem 269: Polynomials with at Least One Integer Root

A root or zero of a polynomial $P(x)$ is a solution to the equation $P(x) = 0$.  
Define $P\_n$ as the polynomial whose coefficients are the digits of $n$.  
For example, $P\_{5703}(x) = 5x^3 + 7x^2 + 3$.

We can see that:

-   $P\_n(0)$ is the last digit of $n$,
-   $P\_n(1)$ is the sum of the digits of $n$,
-   $P\_n(10)$ is $n$ itself.

Define $Z(k)$ as the number of positive integers, $n$, not exceeding $k$ for which the polynomial $P\_n$ has at least one integer root.

It can be verified that $Z(100\\,000)$ is $14696$.

What is $Z(10^{16})$?
