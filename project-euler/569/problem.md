# Problem 569: Prime Mountain Range

A mountain range consists of a line of mountains with slopes of exactly $45^\\circ$, and heights governed by the prime numbers, $p\_n$. The up-slope of the $k$<sup>th</sup> mountain is of height $p\_{2k - 1}$, and the downslope is $p\_{2k}$. The first few foot-hills of this range are illustrated below.

![0569-prime-mountain-range.gif](./png/001.gif)

Tenzing sets out to climb each one in turn, starting from the lowest. At the top of each peak, he looks back and counts how many of the previous peaks he can see. In the example above, the eye-line from the third mountain is drawn in red, showing that he can only see the peak of the second mountain from this viewpoint. Similarly, from the $9$<sup>th</sup> mountain, he can see three peaks, those of the $5$<sup>th</sup>, $7$<sup>th</sup> and $8$<sup>th</sup> mountain.

Let $P(k)$ be the number of peaks that are visible looking back from the $k$<sup>th</sup> mountain. Hence $P(3)=1$ and $P(9)=3$.  
Also $\\displaystyle \\sum\_{k=1}^{100} P(k) = 227$.

Find $\\displaystyle \\sum\_{k=1}^{2500000} P(k)$.
