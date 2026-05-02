# Problem 573: Unfair Race

$n$ runners in very different training states want to compete in a race. Each one of them is given a different starting number $k$ $(1\\leq k \\leq n)$ according to the runner's (constant) individual racing speed being $v\_k=\\frac{k}{n}$.  
In order to give the slower runners a chance to win the race, $n$ different starting positions are chosen randomly (with uniform distribution) and independently from each other within the racing track of length $1$. After this, the starting position nearest to the goal is assigned to runner $1$, the next nearest starting position to runner $2$ and so on, until finally the starting position furthest away from the goal is assigned to runner $n$. The winner of the race is the runner who reaches the goal first.

Interestingly, the expected running time for the winner is $\\frac{1}{2}$, independently of the number of runners. Moreover, while it can be shown that all runners will have the same expected running time of $\\frac{n}{n+1}$, the race is still unfair, since the winning chances may differ significantly for different starting numbers:

Let $P\_{n,k}$ be the probability for runner $k$ to win a race with $n$ runners and $E\_n = \\sum\_{k=1}^n k P\_{n,k}$ be the expected starting number of the winner in that race. It can be shown that, for example, $P\_{3,1}=\\frac{4}{9}$, $P\_{3,2}=\\frac{2}{9}$, $P\_{3,3}=\\frac{1}{3}$ and $E\_3=\\frac{17}{9}$ for a race with $3$ runners.  
You are given that $E\_4=2.21875$, $E\_5=2.5104$ and $E\_{10}=3.66021568$.

Find $E\_{1000000}$ rounded to $4$ digits after the decimal point.
