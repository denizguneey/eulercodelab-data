# Problem 981: The Quaternion Group II

Starting from an empty string, we want to build a string with letters "x", "y", "z". At each step, one of the following operations is performed:

-   insert two consecutive identical letters "xx", "yy" or "zz" anywhere into the string;
-   replace one letter in the string with two consecutive letters, according to the rule: "x" $\\to$ "yz", "y" $\\to$ "zx", "z" $\\to$ "xy";
-   exchange two consecutive **different** letters in the string, e.g. "xy" $\\to$ "yx", "zx" $\\to$ "xz", etc.

A string is called neutral if it is possible to produce the string from the empty string after an **even** number of steps.

Let $N(X, Y, Z)$ be the number of neutral strings which contain $X$ copies of "x", $Y$ copies of "y" and $Z$ copies of "z".  
For example, $N(2, 2, 2) = 42$ and $N(8, 8, 8) = 4732773210$.

Find the sum of $N(i^3, j^3, k^3)$ for $0 \\le i, j, k \\lt 88$. Give your answer modulo $888\\,888\\,883$.
