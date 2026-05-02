# Problem 928: Cribbage

This problem is based on (but not identical to) the scoring for the card game [Cribbage](https://en.wikipedia.org/wiki/Cribbage).

Consider a normal pack of $52$ cards. A Hand is a selection of one or more of these cards.

For each Hand the _Hand score_ is the sum of the values of the cards in the Hand where the value of Aces is $1$ and the value of court cards (Jack, Queen, King) is $10$.

The _Cribbage score_ is obtained for a Hand by adding together the scores for:

-   Pairs. A pair is two cards of the same rank. Every pair is worth $2$ points.
-   Runs. A run is a set of at least $3$ cards whose ranks are consecutive, e.g. 9, 10, Jack. Note that Ace is never high, so Queen, King, Ace is **not** a valid run. The number of points for each run is the size of the run. All locally maximum runs are counted. For example, 2, 3, 4, 5, 7, 8, 9 the two runs of 2, 3, 4, 5 and 7, 8, 9 are counted but not 2, 3, 4 or 3, 4, 5.
-   Fifteens. A fifteen is a combination of cards that has value adding to $15$. Every fifteen is worth $2$ points. For this purpose the value of the cards is the same as in the Hand Score.

For example, $(5 \\spadesuit, 5 \\clubsuit, 5 \\diamondsuit, K \\heartsuit)$ has a Cribbage score of $14$ as there are four ways that fifteen can be made and also three pairs can be made.

The example $( A \\diamondsuit, A \\heartsuit, 2 \\clubsuit, 3 \\heartsuit, 4 \\clubsuit, 5 \\spadesuit)$ has a Cribbage score of $16$: two runs of five worth $10$ points, two ways of getting fifteen worth $4$ points and one pair worth $2$ points. In this example the Hand score is equal to the Cribbage score.

Find the number of Hands in a normal pack of cards where the Hand score is equal to the Cribbage score.
