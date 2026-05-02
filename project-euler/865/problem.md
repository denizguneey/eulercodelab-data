# Problem 865: Triplicate Numbers

A triplicate number is a positive integer such that, after repeatedly removing three consecutive identical digits from it, all its digits can be removed.

For example, the integer $122555211$ is a triplicate number: $$122{\\color{red}555}211 \\rightarrow 1{\\color{red}222}11\\rightarrow{\\color{red}111}\\rightarrow.$$ On the other hand, neither $663633$ nor $9990$ are triplicate numbers.

Let $T(n)$ be how many triplicate numbers are less than $10^n$.

For example, $T(6) = 261$ and $T(30) = 5576195181577716$.

Find $T(10^4)$. Give your answer modulo $998244353$.
