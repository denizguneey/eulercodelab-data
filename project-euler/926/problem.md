# Problem 926: Total Roundness

A **round number** is a number that ends with one or more zeros in a given base.

Let us define the roundness of a number $n$ in base $b$ as the number of zeros at the end of the base $b$ representation of $n$.  
For example, $20$ has roundness $2$ in base $2$, because the base $2$ representation of $20$ is $10100$, which ends with $2$ zeros.

Also define $R(n)$, the total roundness of a number $n$, as the sum of the roundness of $n$ in base $b$ for all $b > 1$.  
For example, $20$ has roundness $2$ in base $2$ and roundness $1$ in base $4$, $5$, $10$, $20$, hence we get $R(20)=6$.  
You are also given $R(10!) = 312$.

Find $R(10\\,000\\,000!)$. Give your answer modulo $10^9 + 7$.
