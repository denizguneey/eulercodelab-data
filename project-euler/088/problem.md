# Problem 088: Product-sum Numbers

A natural number, $N$, that can be written as the sum and product of a given set of at least two natural numbers, $\\{a\_1, a\_2, \\dots, a\_k\\}$ is called a product-sum number: $N = a\_1 + a\_2 + \\cdots + a\_k = a\_1 \\times a\_2 \\times \\cdots \\times a\_k$.

For example, $6 = 1 + 2 + 3 = 1 \\times 2 \\times 3$.

For a given set of size, $k$, we shall call the smallest $N$ with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, $k = 2, 3, 4, 5$, and $6$ are as follows.

-   $k=2$: $4 = 2 \\times 2 = 2 + 2$
-   $k=3$: $6 = 1 \\times 2 \\times 3 = 1 + 2 + 3$
-   $k=4$: $8 = 1 \\times 1 \\times 2 \\times 4 = 1 + 1 + 2 + 4$
-   $k=5$: $8 = 1 \\times 1 \\times 2 \\times 2 \\times 2 = 1 + 1 + 2 + 2 + 2$
-   $k=6$: $12 = 1 \\times 1 \\times 1 \\times 1 \\times 2 \\times 6 = 1 + 1 + 1 + 1 + 2 + 6$

Hence for $2 \\le k \\le 6$, the sum of all the minimal product-sum numbers is $4+6+8+12 = 30$; note that $8$ is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for $2 \\le k \\le 12$ is $\\{4, 6, 8, 12, 15, 16\\}$, the sum is $61$.

What is the sum of all the minimal product-sum numbers for $2 \\le k \\le 12000$?
