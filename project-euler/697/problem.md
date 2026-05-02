# Problem 697: Randomly Decaying Sequence

Given a fixed real number $c$, define a random sequence $(X\_n)\_{n\\ge 0}$ by the following random process:

-   $X\_0 = c$ (with probability 1).
-   For $n>0$, $X\_n = U\_n X\_{n-1}$ where $U\_n$ is a real number chosen at random between zero and one, uniformly, and independently of all previous choices $(U\_m)\_{m<n}$.

If we desire there to be precisely a 25% probability that $X\_{100}<1$, then this can be arranged by fixing $c$ such that $\\log\_{10} c \\approx 46.27$.

Suppose now that $c$ is set to a different value, so that there is precisely a 25% probability that $X\_{10\\,000\\,000}<1$.

Find $\\log\_{10} c$ and give your answer rounded to two places after the decimal point.
