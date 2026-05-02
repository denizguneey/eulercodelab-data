# Problem 756: Approximating a Sum

Consider a function $f(k)$ defined for all positive integers $k>0$. Let $S$ be the sum of the first $n$ values of $f$. That is, $$S=f(1)+f(2)+f(3)+\\cdots+f(n)=\\sum\_{k=1}^n f(k).$$

In this problem, we employ randomness to approximate this sum. That is, we choose a random, uniformly distributed, $m$-tuple of positive integers $(X\_1,X\_2,X\_3,\\cdots,X\_m)$ such that $0=X\_0 \\lt X\_1 \\lt X\_2 \\lt \\cdots \\lt X\_m \\leq n$ and calculate a modified sum $S^\*$ as follows. $$S^\* = \\sum\_{i=1}^m f(X\_i)(X\_i-X\_{i-1})$$

We now define the error of this approximation to be $\\Delta=S-S^\*$.

Let $\\mathbb{E}(\\Delta|f(k),n,m)$ be the expected value of the error given the function $f(k)$, the number of terms $n$ in the sum and the length of random sample $m$.

For example, $\\mathbb{E}(\\Delta|k,100,50) = 2525/1326 \\approx 1.904223$ and $\\mathbb{E}(\\Delta|\\varphi(k),10^4,10^2)\\approx 5842.849907$, where $\\varphi(k)$ is Euler's totient function.

Find $\\mathbb{E}(\\Delta|\\varphi(k),12345678,12345)$ rounded to six places after the decimal point.
