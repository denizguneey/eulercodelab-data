# Problem 978: Random Walk Skewness

In this problem we consider a **random walk** on the integers $\\mathbb{Z}$, in which our position at time $t$ is denoted as $X\_t$.

At time $0$ we start at position $0$. That is, $X\_0=0$.  
At time $1$ we jump to position $1$. That is, $X\_1=1$.  
Thereafter, at time $t=2,3,\\dots$ we make a jump of size $|X\_{t-2}|$ in either the positive or negative direction, with probability $1/2$ each way. If $X\_{t-2}=0$ we stay put at time $t$.

At $t=5$ we find our position $X\_5$ has the following distribution: $$ X\_5=\\begin{cases} -1\\quad&\\text{with probability }3/8\\\\ 1\\quad&\\text{with probability }3/8\\\\ 3\\quad&\\text{with probability }1/8\\\\ 5\\quad&\\text{with probability }1/8\\\\ \\end{cases} $$ The **standard deviation** $\\sigma$ of a **random variable** $X$ with **mean** $\\mu$ is defined as $$ \\sigma=\\sqrt{\\mathbb{E}\[X^2\]-\\mu^2} $$ Furthermore the **skewness** of $X$ is defined as $$ \\text{Skew}(X)=\\mathbb{E}\\biggl\[\\Bigl(\\frac{X-\\mu}{\\sigma}\\Bigr)^3\\biggr\] $$ For $X\_5$, which has mean $1$ and standard deviation $2$, we find $\\text{Skew}(X\_5)=0.75$. You are also given $\\text{Skew}(X\_{10})\\approx2.50997097$.

Find $\\text{Skew}(X\_{50})$. Give your answer rounded to eight digits after the decimal point.
