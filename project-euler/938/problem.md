# Problem 938: Exhausting a Colour

A deck of cards contains $R$ red cards and $B$ black cards.  
A card is chosen uniformly randomly from the deck and removed. A second card is then chosen uniformly randomly from the cards remaining and removed.

-   If both cards are red, they are discarded.
-   If both cards are black, they are both put back in the deck.
-   If they are different colours, the red card is put back in the deck and the black card is discarded.

Play ends when all the remaining cards in the deck are the same colour and let $P(R,B)$ be the probability that this colour is black.

You are given $P(2,2) = 0.4666666667$, $P(10,9) = 0.4118903397$ and $P(34,25) = 0.3665688069$.

Find $P(24690,12345)$. Give your answer with 10 digits after the decimal point.
