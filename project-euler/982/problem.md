# Problem 982: The Third Dice

Alice and Bob play the following game with two six-sided dice (numbered $1$ to $6$):

1.  Alice rolls both dice; she can see the rolled values but Bob cannot
2.  Alice chooses one of the dice and reveals it to Bob
3.  Bob chooses one of the dice: either the one he can see, or the one he cannot
4.  Alice pays Bob the value shown on Bob's chosen dice

Each player devises a (possibly non-deterministic) **strategy**. An example strategy for each player could be:

-   Alice chooses to reveal the dice with value closest to $3.5$, or if both are equidistant she chooses randomly with equal probability
-   Bob chooses the revealed dice if its value is at least $4$; otherwise he chooses the hidden dice

In fact, these two strategies together form a **Nash equilibrium**. That is, given that Bob is using his strategy, Alice's strategy **minimises** the expected payment; and given that Alice is using her strategy, Bob's strategy **maximises** the expected payment.

With these strategies the expected payment from Alice to Bob is $\\frac{145}{36}\\approx 4.027778$.

To make the game more interesting, they introduce a third (six-sided) dice:

1.  Alice rolls **three** dice; she can see the rolled values but Bob cannot
2.  Alice chooses **two** of the dice and reveals both to Bob
3.  Bob chooses one of the three dice: either one of the two visible dice, or the one hidden dice
4.  Alice pays Bob the value shown on Bob's chosen dice

Supposing they settle on a pair of strategies that form a Nash equilibrium, find the expected payment from Alice to Bob, and give your answer rounded to six digits after the decimal point.
