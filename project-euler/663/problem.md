# Problem 663: Sums of Subarrays

Let $t\_k$ be the **tribonacci numbers** defined as:  
$\\quad t\_0 = t\_1 = 0$;  
$\\quad t\_2 = 1$;  
$\\quad t\_k = t\_{k-1} + t\_{k-2} + t\_{k-3} \\quad \\text{ for } k \\ge 3$.

For a given integer $n$, let $A\_n$ be an array of length $n$ (indexed from $0$ to $n-1$), that is initially filled with zeros.  
The array is changed iteratively by replacing $A\_n\[(t\_{2 i-2} \\bmod n)\]$ with $A\_n\[(t\_{2 i-2} \\bmod n)\]+2 (t\_{2 i-1} \\bmod n)-n+1$ in each step $i$.  
After each step $i$, define $M\_n(i)$ to be $\\displaystyle \\max\\{\\sum\_{j=p}^q A\_n\[j\]: 0\\le p\\le q \\lt n\\}$, the maximal sum of any contiguous subarray of $A\_n$.

The first 6 steps for $n=5$ are illustrated below:  
Initial state: $\\, A\_5=\\{0,0,0,0,0\\}$  
Step 1: $\\quad \\Rightarrow A\_5=\\{-4,0,0,0,0\\}$, $M\_5(1)=0$  
Step 2: $\\quad \\Rightarrow A\_5=\\{-4, -2, 0, 0, 0\\}$, $M\_5(2)=0$  
Step 3: $\\quad \\Rightarrow A\_5=\\{-4, -2, 4, 0, 0\\}$, $M\_5(3)=4$  
Step 4: $\\quad \\Rightarrow A\_5=\\{-4, -2, 6, 0, 0\\}$, $M\_5(4)=6$  
Step 5: $\\quad \\Rightarrow A\_5=\\{-4, -2, 6, 0, 4\\}$, $M\_5(5)=10$  
Step 6: $\\quad \\Rightarrow A\_5=\\{-4, 2, 6, 0, 4\\}$, $M\_5(6)=12$  

Let $\\displaystyle S(n,l)=\\sum\_{i=1}^l M\_n(i)$. Thus $S(5,6)=32$.  
You are given $S(5,100)=2416$, $S(14,100)=3881$ and $S(107,1000)=1618572$.

Find $S(10\\,000\\,003,10\\,200\\,000)-S(10\\,000\\,003,10\\,000\\,000)$.
