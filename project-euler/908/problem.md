# Problem 908: Clock Sequence II

A clock sequence is a periodic sequence of positive integers that can be broken into contiguous segments such that the sum of the $n$-th segment is equal to $n$.

For example, the sequence $$1\\ 2\\ 3\\ 4\\ 3\\ 2\\ 1\\ 2\\ 3\\ 4\\ 3\\ 2\\ 1\\ 2\\ 3\\ 4\\ 3\\ 2\\ 1\\ \\cdots$$ is a clock sequence with period $6$, as it can be broken into $$1\\Big |2\\Big |3\\Big |4\\Big |3\\ 2\\Big |1\\ 2\\ 3\\Big |4\\ 3\\Big |2\\ 1\\ 2\\ 3\\Big |4\\ 3\\ 2\\Big |1\\ 2\\ 3\\ 4\\Big |3\\ 2\\ 1\\ 2\\ 3\\Big |\\cdots$$ Let $C(N)$ be the number of different clock sequences with period at most $N$. For example, $C(3) = 3$, $C(4) = 7$ and $C(10) = 561$.

Find $C(10^4) \\bmod 1111211113$.
