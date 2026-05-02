# Problem 483: Repeated Permutation

We define a permutation as an operation that rearranges the order of the elements $\\{1, 2, 3, ..., n\\}$. There are $n!$ such permutations, one of which leaves the elements in their initial order. For $n = 3$ we have $3! = 6$ permutations:

-   $P\_1 =$ keep the initial order
-   $P\_2 =$ exchange the 1<sup>st</sup> and 2<sup>nd</sup> elements
-   $P\_3 =$ exchange the 1<sup>st</sup> and 3<sup>rd</sup> elements
-   $P\_4 =$ exchange the 2<sup>nd</sup> and 3<sup>rd</sup> elements
-   $P\_5 =$ rotate the elements to the right
-   $P\_6 =$ rotate the elements to the left

If we select one of these permutations, and we re-apply the same permutation repeatedly, we eventually restore the initial order.  
For a permutation $P\_i$, let $f(P\_i)$ be the number of steps required to restore the initial order by applying the permutation $P\_i$ repeatedly.  
For $n = 3$, we obtain:

-   $f(P\_1) = 1$ : $(1,2,3) \\to (1,2,3)$
-   $f(P\_2) = 2$ : $(1,2,3) \\to (2,1,3) \\to (1,2,3)$
-   $f(P\_3) = 2$ : $(1,2,3) \\to (3,2,1) \\to (1,2,3)$
-   $f(P\_4) = 2$ : $(1,2,3) \\to (1,3,2) \\to (1,2,3)$
-   $f(P\_5) = 3$ : $(1,2,3) \\to (3,1,2) \\to (2,3,1) \\to (1,2,3)$
-   $f(P\_6) = 3$ : $(1,2,3) \\to (2,3,1) \\to (3,1,2) \\to (1,2,3)$

Let $g(n)$ be the average value of $f^2(P\_i)$ over all permutations $P\_i$ of length $n$.  
$g(3) = (1^2 + 2^2 + 2^2 + 2^2 + 3^2 + 3^2)/3! = 31/6 \\approx 5.166666667\\mathrm e0$  
$g(5) = 2081/120 \\approx 1.734166667\\mathrm e1$  
$g(20) = 12422728886023769167301/2432902008176640000 \\approx 5.106136147\\mathrm e3$

Find $g(350)$ and write the answer in scientific notation rounded to $10$ significant digits, using a lowercase e to separate mantissa and exponent, as in the examples above.
