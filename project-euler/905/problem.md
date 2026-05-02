# Problem 905: Now I Know

Three epistemologists, known as A, B, and C, are in a room, each wearing a hat with a number on it. They have been informed beforehand that all three numbers are positive and that one of the numbers is the sum of the other two.

Once in the room, they can see the numbers on each other's hats but not on their own. Starting with A and proceeding cyclically, each epistemologist must either honestly state "I don't know my number" or announce "Now I know my number!" which terminates the game.

For instance, if their numbers are $A=2, B=1, C=1$ then A declares "Now I know" at the first turn. If their numbers are $A=2, B=7, C=5$ then "I don't know" is heard four times before B finally declares "Now I know" at the fifth turn.

Let $F(A,B,C)$ be the number of turns it takes until an epistemologist declares "Now I know", including the turn this declaration is made. So $F(2,1,1)=1$ and $F(2,7,5)=5$.

Find $\\displaystyle \\sum\_{a=1}^7 \\sum\_{b=1}^{19} F(a^b, b^a, a^b + b^a)$.
