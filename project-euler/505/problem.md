# Problem 505: Bidirectional Recurrence

Let:

$\\begin{array}{ll} x(0)&=0 \\\\ x(1)&=1 \\\\ x(2k)&=(3x(k)+2x(\\lfloor \\frac k 2 \\rfloor)) \\text{ mod } 2^{60} \\text{ for } k \\ge 1 \\text {, where } \\lfloor \\text { } \\rfloor \\text { is the floor function} \\\\ x(2k+1)&=(2x(k)+3x(\\lfloor \\frac k 2 \\rfloor)) \\text{ mod } 2^{60} \\text{ for } k \\ge 1 \\\\ y\_n(k)&=\\left\\{{\\begin{array}{lc} x(k) && \\text{if } k \\ge n \\\\ 2^{60} - 1 - max(y\_n(2k),y\_n(2k+1)) && \\text{if } k < n \\end{array}} \\right. \\\\ A(n)&=y\_n(1) \\end{array}$

You are given:

$\\begin{array}{ll} x(2)&=3 \\\\ x(3)&=2 \\\\ x(4)&=11 \\\\ y\_4(4)&=11 \\\\ y\_4(3)&=2^{60}-9\\\\ y\_4(2)&=2^{60}-12 \\\\ y\_4(1)&=A(4)=8 \\\\ A(10)&=2^{60}-34\\\\ A(10^3)&=101881 \\end{array}$

Find $A(10^{12})$.
