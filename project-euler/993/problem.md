# Problem 993: Banana Beaver

A beaver plays a game on an infinitely long number line.  
When the game starts, the beaver is at position $0$, carrying $N$ bananas, and there are no other bananas on the number line.  
At each step, the beaver will do the following according to the bananas it sees at positions $x$ and $x + 1$, where $x$ is the beaver's current position:

-   If there is a banana at $x$ and another banana at $x + 1$, then the beaver will pick up a banana at position $x+1$, and then move itself to position $x-1$.
-   If there is a banana at $x$ but there is no banana at $x+1$, then it will pick up a banana at $x$ and move itself to position $x+2$.
-   If there is no banana at $x$ but there is a banana at $x+1$, then it will move a banana from position $x+1$ to position $x$ and move itself to position $x+2$.
-   If there is no banana at $x$ and no banana at $x + 1$, then the beaver checks whether it still carries at least three bananas. If so, then it will drop a banana at each of the three positions $x - 1, x, x + 1$ and move itself to position $x-2$; otherwise the game ends.

For example, if $N \\ge 3$, then the last rule applies to the starting position, so after $1$ step, there are $3$ bananas on the number line, at positions $-1, 0, 1$, with the beaver at position $-2$.  
Similarly, if $N \\ge 5$, then after $5$ steps, there are $5$ bananas on the number line, at positions $-2,-1,0,1,2$, with the beaver at position $-1$.

Let $\\operatorname{BB}(N)$ be the position of the beaver when the game ends (which can be proved to always happen).  
You are given $\\operatorname{BB}(1000) = 1499$.

Find $\\operatorname{BB}(10^{18})$.
