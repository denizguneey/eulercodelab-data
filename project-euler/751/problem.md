# Problem 751: Concatenation Coincidence

A non-decreasing sequence of integers $a\_n$ can be generated from any positive real value $\\theta$ by the following procedure: $$\\begin{align} \\begin{split} b\_1 &= \\theta \\\\ b\_n &= \\left\\lfloor b\_{n-1} \\right\\rfloor \\left(b\_{n-1} - \\left\\lfloor b\_{n-1} \\right\\rfloor + 1\\right)~~~\\forall ~ n \\geq 2 \\\\ a\_n &= \\left\\lfloor b\_{n} \\right\\rfloor \\end{split} \\end{align}$$ Where $\\left\\lfloor \\cdot \\right\\rfloor$ is the floor function.

For example, $\\theta=2.956938891377988...$ generates the Fibonacci sequence: $2, 3, 5, 8, 13, 21, 34, 55, 89, ...$

The _concatenation_ of a sequence of positive integers $a\_n$ is a real value denoted $\\tau$ constructed by concatenating the elements of the sequence after the decimal point, starting at $a\_1$: $a\_1.a\_2a\_3a\_4...$

For example, the Fibonacci sequence constructed from $\\theta=2.956938891377988...$ yields the concatenation $\\tau=2.3581321345589...$ Clearly, $\\tau \\neq \\theta$ for this value of $\\theta$.

Find the only value of $\\theta$ for which the generated sequence starts at $a\_1=2$ and the concatenation of the generated sequence equals the original value: $\\tau = \\theta$. Give your answer rounded to $24$ places after the decimal point.
