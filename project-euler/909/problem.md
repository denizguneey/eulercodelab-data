# Problem 909: L-expressions I

An L-expression is defined as any one of the following:

-   a natural number;
-   the symbol $A$;
-   the symbol $Z$;
-   the symbol $S$;
-   a pair of L-expressions $u, v$, which is written as $u(v)$.

An L-expression can be transformed according to the following rules:

-   $A(x) \\to x + 1$ for any natural number $x$;
-   $Z(u)(v) \\to v$ for any L-expressions $u, v$;
-   $S(u)(v)(w) \\to v(u(v)(w))$ for any L-expressions $u, v, w$.

For example, after applying all possible rules, the L-expression $S(Z)(A)(0)$ is transformed to the number $1$: $$S(Z)(A)(0) \\to A(Z(A)(0)) \\to A(0) \\to 1.$$ Similarly, the L-expression $S(S)(S(S))(S(Z))(A)(0)$ is transformed to the number $6$ after applying all possible rules.

Find the result of the L-expression $S(S)(S(S))(S(S))(S(Z))(A)(0)$ after applying all possible rules. Give the last nine digits as your answer.

**Note:** it can be proved that the L-expression in question can only be transformed a finite number of times, and the final result does not depend on the order of the transformations.
