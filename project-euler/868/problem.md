# Problem 868: Belfry Maths

There is a method that is used by Bell ringers to generate all variations of the order that bells are rung.

The same method can be used to create all permutations of a set of letters. Consider the letters to be permuted initially in order from smallest to largest. At each step swap the largest letter with the letter on its left or right whichever generates a permutation that has not yet been seen. If neither gives a new permutation then try the next largest letter and so on. This procedure continues until all permutations have been generated.

For example, $3$ swaps are required to reach the permutation CBA when starting with ABC.  
The swaps are ABC $\\to$ ACB $\\to$ CAB $\\to$ CBA.  
Also $59$ swaps are required to reach BELFRY when starting with these letters in alphabetical order.

Find the number of swaps that are required to reach NOWPICKBELFRYMATHS when starting with these letters in alphabetical order.
