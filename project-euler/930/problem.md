# Problem 930: The Gathering

Given $n\\ge 2$ bowls arranged in a circle, $m\\ge 2$ balls are distributed amongst them.

Initially the balls are distributed randomly: for each ball, a bowl is chosen equiprobably and independently of the other balls. After this is done, we start the following process:

1.  Choose one of the $m$ balls equiprobably at random.
2.  Choose a direction to move - either clockwise or anticlockwise - again equiprobably at random.
3.  Move the chosen ball to the neighbouring bowl in the chosen direction.
4.  Return to step 1.

This process stops when all the $m$ balls are located in the same bowl. Note that this may be after zero steps, if the balls happen to have been initially distributed all in the same bowl.

Let $F(n, m)$ be the expected number of times we move a ball before the process stops. For example, $F(2, 2) = \\frac{1}{2}$, $F(3, 2) = \\frac{4}{3}$, $F(2, 3) = \\frac{9}{4}$, and $F(4, 5) = \\frac{6875}{24}$.

Let $G(N, M) = \\sum\_{n=2}^N \\sum\_{m=2}^M F(n, m)$. For example, $G(3, 3) = \\frac{137}{12}$ and $G(4, 5) = \\frac{6277}{12}$. You are also given that $G(6, 6) \\approx 1.681521567954e4$ in scientific format with 12 significant digits after the decimal point.

Find $G(12, 12)$. Give your answer in scientific format with 12 significant digits after the decimal point.
