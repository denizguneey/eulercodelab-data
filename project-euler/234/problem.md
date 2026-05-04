# Problem 234: Semidivisible Numbers

For an integer $n \\ge 4$, we define the lower prime square root of $n$, denoted by $\\mathrm{lps}(n)$, as the largest prime $\\le \\sqrt n$ and the upper prime square root of $n$, $\\mathrm{ups}(n)$, as the smallest prime $\\ge \\sqrt n$.

So, for example, $\\mathrm{lps}(4) = 2 = \\mathrm{ups}(4)$, $\\mathrm{lps}(1000) = 31$, $\\mathrm{ups}(1000) = 37$.  
Let us call an integer $n \\ge 4$ semidivisible, if one of $\\mathrm{lps}(n)$ and $\\mathrm{ups}(n)$ divides $n$, but not both.

The sum of the semidivisible numbers not exceeding $15$ is $30$, the numbers are $8$, $10$ and $12$.  
$15$ is not semidivisible because it is a multiple of both $\\mathrm{lps}(15) = 3$ and $\\mathrm{ups}(15) = 5$.  
As a further example, the sum of the $92$ semidivisible numbers up to $1000$ is $34825$.

What is the sum of all semidivisible numbers not exceeding $999966663333$?
