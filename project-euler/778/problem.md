# Problem 778: Freshman's Product

If $a,b$ are two nonnegative integers with decimal representations $a=(\\dots a\_2a\_1a\_0)$ and $b=(\\dots b\_2b\_1b\_0)$ respectively, then the _freshman's product_ of $a$ and $b$, denoted $a\\boxtimes b$, is the integer $c$ with decimal representation $c=(\\dots c\_2c\_1c\_0)$ such that $c\_i$ is the last digit of $a\_i\\cdot b\_i$.  
For example, $234 \\boxtimes 765 = 480$.

Let $F(R,M)$ be the sum of $x\_1 \\boxtimes \\dots \\boxtimes x\_R$ for all sequences of integers $(x\_1,\\dots,x\_R)$ with $0\\leq x\_i \\leq M$.  
For example, $F(2, 7) = 204$, and $F(23, 76) \\equiv 5870548 \\pmod{ 1\\,000\\,000\\,009}$.

Find $F(234567,765432)$. Give your answer modulo $1\\,000\\,000\\,009$.
