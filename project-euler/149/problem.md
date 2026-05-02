# Problem 149: Maximum-sum Subsequence

Looking at the table below, it is easy to verify that the maximum possible sum of adjacent numbers in any direction (horizontal, vertical, diagonal or anti-diagonal) is $16$ ($= 8 + 7 + 1$).

<table border="1" cellpadding="6" cellspacing="0" style="margin:auto;"><tbody align="right"><tr><td width="25">$-2$</td><td width="25">$5$</td><td width="25">$3$</td><td width="25">$2$</td></tr><tr><td>$9$</td><td>$-6$</td><td>$5$</td><td>$1$</td></tr><tr><td>$3$</td><td>$2$</td><td>$7$</td><td>$3$</td></tr><tr><td>$-1$</td><td>$8$</td><td>$-4$</td><td>$8$</td></tr></tbody></table>

Now, let us repeat the search, but on a much larger scale:

First, generate four million pseudo-random numbers using a specific form of what is known as a "Lagged Fibonacci Generator":

For $1 \\le k \\le 55$, $s\_k = \[100003 - 200003 k + 300007 k^3\] \\pmod{1000000} - 500000$.  
For $56 \\le k \\le 4000000$, $s\_k = \[s\_{k-24} + s\_{k - 55} + 1000000\] \\pmod{1000000} - 500000$.

Thus, $s\_{10} = -393027$ and $s\_{100} = 86613$.

The terms of $s$ are then arranged in a $2000 \\times 2000$ table, using the first $2000$ numbers to fill the first row (sequentially), the next $2000$ numbers to fill the second row, and so on.

Finally, find the greatest sum of (any number of) adjacent entries in any direction (horizontal, vertical, diagonal or anti-diagonal).
