# Problem 988: Non-attacking Frogs

Frogs can be placed on the real number line at integer locations. Given coprime positive integers $(a,b)$, each frog has the ability to make jumps of distances $a$ or $b$ in the positive direction.

Two frogs placed at $m$ and $n$, $m<n$, are _attacking_ if the frog at $m$ can hop to $n$ with some series of jumps. For example if $(a,b)=(3,5)$, frogs placed at $0$ and $11$ are attacking as the former can make two jumps of $3$ and one jump of $5$ to reach $11$. However, frogs placed at $4$ and $11$ are non-attacking.

A _non-attacking configuration_ is a placement of any number of frogs such that:

-   one frog is placed at $0$;
-   all other frogs are placed at distinct positive integers;
-   no two frogs are attacking.

Define $F(a,b)$ to be sum of the integer locations of every frog, summing over all non-attacking configurations. For example if $(a,b)=(3,5)$ there are seven non-attacking configurations: $$\\{0\\}\\quad\\quad\\{0,1\\}\\quad\\quad\\{0,2\\}\\quad\\quad\\{0,4\\}\\quad\\quad\\{0,7\\}\\quad\\quad\\{0,1,2\\}\\quad\\quad\\{0,2,4\\} $$giving $F(3,5)=23$.

You are also given $F(5,13)=16336$.

Find $F(19,53)$.
