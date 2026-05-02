# Problem 904: Pythagorean Angle

Given a right-angled triangle with integer sides, the smaller angle formed by the two medians drawn on the the two perpendicular sides is denoted by $\\theta$.

![0904\_Pythagorean\_angle.jpg](./png/001.png)

Let $f(\\alpha, L)$ denote the sum of the sides of the right-angled triangle minimizing the absolute difference between $\\theta$ and $\\alpha$ among all right-angled triangles with integer sides and hypotenuse not exceeding $L$.  
If more than one triangle attains the minimum value, the triangle with the maximum area is chosen. All angles in this problem are measured in degrees.

For example, $f(30,10^2)=198$ and $f(10,10^6)= 1600158$.

Define $F(N,L)=\\sum\_{n=1}^{N}f\\left(\\sqrt\[3\]{n},L\\right)$.  
You are given $F(10,10^6)= 16684370$.

Find $F(45000, 10^{10})$.
