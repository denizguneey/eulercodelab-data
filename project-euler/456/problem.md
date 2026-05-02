# Problem 456: Triangles Containing the Origin II

Define:  
$x\_n = (1248^n \\bmod 32323) - 16161$  
$y\_n = (8421^n \\bmod 30103) - 15051$  
$P\_n = \\{(x\_1, y\_1), (x\_2, y\_2), \\dots, (x\_n, y\_n)\\}$

For example, $P\_8 = \\{(-14913, -6630),$$(-10161, 5625),$$(5226, 11896),$$(8340, -10778),$$(15852, -5203),$$(-15165, 11295),$$(-1427, -14495),$$(12407, 1060)\\}$.

Let $C(n)$ be the number of triangles whose vertices are in $P\_n$ which contain the origin in the interior.

Examples:  
$C(8) = 20$  
$C(600) = 8950634$  
$C(40\\,000) = 2666610948988$

Find $C(2\\,000\\,000)$.
