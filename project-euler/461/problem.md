# Problem 461: Almost Pi

Let $f\_n(k) = e^{k/n} - 1$, for all non-negative integers $k$.

Remarkably, $f\_{200}(6)+f\_{200}(75)+f\_{200}(89)+f\_{200}(226)=\\underline{3.1415926}44529\\cdots\\approx\\pi$.

In fact, it is the best approximation of $\\pi$ of the form $f\_n(a) + f\_n(b) + f\_n(c) + f\_n(d)$ for $n=200$.

Let $g(n)=a^2 + b^2 + c^2 + d^2$ for $a, b, c, d$ that minimize the error: $|f\_n(a) + f\_n(b) + f\_n(c) + f\_n(d) - \\pi|$  
(where $|x|$ denotes the absolute value of $x$).

You are given $g(200)=6^2+75^2+89^2+226^2=64658$.

Find $g(10000)$.
