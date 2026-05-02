# Problem 736: Paths to Equality

Define two functions on lattice points:

$r(x,y) = (x+1,2y)$

$s(x,y) = (2x,y+1)$

A _path to equality_ of length $n$ for a pair $(a,b)$ is a sequence $\\Big((a\_1,b\_1),(a\_2,b\_2),\\ldots,(a\_n,b\_n)\\Big)$, where:

-   $(a\_1,b\_1) = (a,b)$
-   $(a\_k,b\_k) = r(a\_{k-1},b\_{k-1})$ or $(a\_k,b\_k) = s(a\_{k-1},b\_{k-1})$ for $k > 1$
-   $a\_k \\ne b\_k$ for $k < n$
-   $a\_n = b\_n$

$a\_n = b\_n$ is called the _final value_.

For example,

$(45,90)\\xrightarrow{r} (46,180)\\xrightarrow{s}(92,181)\\xrightarrow{s}(184,182)\\xrightarrow{s}(368,183)\\xrightarrow{s}(736,184)\\xrightarrow{r}$

$(737,368)\\xrightarrow{s}(1474,369)\\xrightarrow{r}(1475,738)\\xrightarrow{r}(1476,1476)$

This is a path to equality for $(45,90)$ and is of length 10 with final value 1476. There is no path to equality of $(45,90)$ with smaller length.

Find the unique path to equality for $(45,90)$ with smallest **odd** length. Enter the final value as your answer.
