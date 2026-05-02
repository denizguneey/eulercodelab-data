# Problem 779: Prime Factor and Exponent

For a positive integer $n \\gt 1$, let $p(n)$ be the smallest prime dividing $n$, and let $\\alpha(n)$ be its **$p$-adic order**, i.e. the largest integer such that $p(n)^{\\alpha(n)}$ divides $n$.

For a positive integer $K$, define the function $f\_K(n)$ by: $$f\_K(n)=\\frac{\\alpha(n)-1}{(p(n))^K}.$$

Also define $\\overline{f\_K}$ by: $$\\overline{f\_K}=\\lim\_{N \\to \\infty} \\frac{1}{N}\\sum\_{n=2}^{N} f\_K(n).$$

It can be verified that $\\overline{f\_1} \\approx 0.282419756159$.

Find $\\displaystyle \\sum\_{K=1}^{\\infty}\\overline{f\_K}$. Give your answer rounded to $12$ digits after the decimal point.
