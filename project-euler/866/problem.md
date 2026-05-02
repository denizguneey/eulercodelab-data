# Problem 866: Tidying Up B

A small child has a “number caterpillar” consisting of $N$ jigsaw pieces, each with one number on it, which, when connected together in a line, reveal the numbers $1$ to $N$ in order.

Every night, the child's father has to pick up the pieces of the caterpillar that have been scattered across the play room. He picks up the pieces at random and places them in the correct order.  
As the caterpillar is built up in this way, it forms distinct segments that gradually merge together.

Any time the father places a new piece in its correct position, a segment of length $k$ is formed and he writes down the $k$<sup>th</sup> hexagonal number $k\\cdot(2k-1)$. Once all pieces have been placed and the full caterpillar constructed he calculates the product of all the numbers written down. Interestingly, the expected value of this product is always an integer. For example if $N=4$ then the expected value is $994$.

Find the expected value of the product for a caterpillar of $N=100$ pieces. Give your answer modulo $987654319$.
