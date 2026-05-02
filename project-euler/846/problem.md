# Problem 846: Magic Bracelets

A _bracelet_ is made by connecting at least three numbered beads in a circle. Each bead can only display $1$, $2$, or any number of the form $p^k$ or $2p^k$ for odd prime $p$.

In addition a _magic bracelet_ must satisfy the following two conditions:

-   no two beads display the same number
-   the product of the numbers of any two adjacent beads is of the form $x^2+1$

![0846\_diagram.jpg](./png/001.jpg)

Define the _potency_ of a magic bracelet to be the sum of numbers on its beads.

The example is a magic bracelet with five beads which has a potency of 155.

Let $F(N)$ be the sum of the potency of each magic bracelet which can be formed using positive integers not exceeding $N$, where rotations and reflections of an arrangement are considered equivalent. You are given $F(20)=258$ and $F(10^2)=538768$.

Find $F(10^6)$.
