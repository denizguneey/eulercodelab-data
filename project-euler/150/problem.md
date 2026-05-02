# Problem 150: Sub-triangle Sums

In a triangular array of positive and negative integers, we wish to find a sub-triangle such that the sum of the numbers it contains is the smallest possible.

In the example below, it can be easily verified that the marked triangle satisfies this condition having a sum of −42.

![](./png/001.gif)

We wish to make such a triangular array with one thousand rows, so we generate 500500 pseudo-random numbers s<sub>k</sub> in the range ±2<sup>19</sup>, using a type of random number generator (known as a Linear Congruential Generator) as follows:

t := 0  
for k = 1 up to k = 500500:  
    t := (615949\*t + 797807) modulo 2<sup>20</sup>  
    s<sub>k</sub> := t−2<sup>19</sup>

Thus: s<sub>1</sub> = 273519, s<sub>2</sub> = −153582, s<sub>3</sub> = 450905 etc

Our triangular array is then formed using the pseudo-random numbers thus:

s<sub>1</sub>  
s<sub>2</sub>  s<sub>3</sub>  
s<sub>4</sub>  s<sub>5</sub>  s<sub>6</sub>   
s<sub>7</sub>  s<sub>8</sub>  s<sub>9</sub>  s<sub>10</sub>  
...

Sub-triangles can start at any element of the array and extend down as far as we like (taking-in the two elements directly below it from the next row, the three elements directly below from the row after that, and so on).  
The "sum of a sub-triangle" is defined as the sum of all the elements it contains.  
Find the smallest possible sub-triangle sum.
