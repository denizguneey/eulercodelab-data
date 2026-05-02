# Problem 901: Well Drilling

A driller drills for water. At each iteration the driller chooses a depth $d$ (a positive real number), drills to this depth and then checks if water was found. If so, the process terminates. Otherwise, a new depth is chosen and a new drilling starts from the ground level in a new location nearby.

Drilling to depth $d$ takes exactly $d$ hours. The groundwater depth is constant in the relevant area and its distribution is known to be an [exponential random variable](https://en.wikipedia.org/wiki/Exponential_distribution) with expected value of $1$. In other words, the probability that the groundwater is deeper than $d$ is $e^{-d}$.

Assuming an optimal strategy, find the minimal expected drilling time in hours required to find water. Give your answer rounded to 9 places after the decimal point.
