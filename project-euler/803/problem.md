# Problem 803: Pseudorandom Sequence

**Rand48** is a pseudorandom number generator used by some programming languages. It generates a sequence from any given integer $0 \\le a\_0 < 2^{48}$ using the rule $a\_n = (25214903917 \\cdot a\_{n - 1} + 11) \\bmod 2^{48}$.

Let $b\_n = \\lfloor a\_n / 2^{16} \\rfloor \\bmod 52$. The sequence $b\_0, b\_1, \\dots$ is translated to an infinite string $c = c\_0c\_1\\dots$ via the rule:  
$0 \\rightarrow$ a, $1\\rightarrow$ b, $\\dots$, $25 \\rightarrow$ z, $26 \\rightarrow$ A, $27 \\rightarrow$ B, $\\dots$, $51 \\rightarrow$ Z.

For example, if we choose $a\_0 = 123456$, then the string $c$ starts with: "bQYicNGCY$\\dots$".  
Moreover, starting from index $100$, we encounter the substring "RxqLBfWzv" for the first time.

Alternatively, if $c$ starts with "EULERcats$\\dots$", then $a\_0$ must be $78580612777175$.

Now suppose that the string $c$ starts with "PuzzleOne$\\dots$".  
Find the starting index of the first occurrence of the substring "LuckyText" in $c$.
