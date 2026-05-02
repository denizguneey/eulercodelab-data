# Problem 990: Addition Equations

A string forms an _addition equation_ if it consists of

-   Digits, forming positive integers. No leading zeros are allowed.
-   A single plus sign between integers.
-   A single equality sign.

Most importantly, the equality must hold.

Example of strings of length 7 forming addition equations:  
1+1+1=3  
100=100  
77=7+70  
1+2=2+1

Note that strings are considered different even if they form equivalent equations, so for example here are three unique strings:  
1+2=3  
2+1=3  
3=1+2

The following strings do not form valid addition equations:  
1+1=3  
1+1=02  
0+1=1  
+1=1  
2-1=1

Let $A(n)$ be the number of strings of length not larger than $n$ forming addition equations.

You are given $A(3) = 9$, $A(5)=171$ and $A(7)=4878$.

Find $A(50)$. Give your answer modulo $10^9 + 7$.
