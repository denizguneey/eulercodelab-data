# Problem 426: Box-Ball System

Consider an infinite row of boxes. Some of the boxes contain a ball. For example, an initial configuration of 2 consecutive occupied boxes followed by 2 empty boxes, 2 occupied boxes, 1 empty box, and 2 occupied boxes can be denoted by the sequence (2, 2, 2, 1, 2), in which the number of consecutive occupied and empty boxes appear alternately.

A turn consists of moving each ball exactly once according to the following rule: Transfer the leftmost ball which has not been moved to the nearest empty box to its right.

After one turn the sequence (2, 2, 2, 1, 2) becomes (2, 2, 1, 2, 3) as can be seen below; note that we begin the new sequence starting at the first occupied box.

![0426\_baxball1.gif](./png/001.gif)

A system like this is called a **Box-Ball System** or **BBS** for short.

It can be shown that after a sufficient number of turns, the system evolves to a state where the consecutive numbers of occupied boxes is invariant. In the example below, the consecutive numbers of **occupied boxes** evolves to \[1, 2, 3\]; we shall call this the final state.

![0426\_baxball2.gif](./png/002.gif)

We define the sequence {t<sub><var>i</var></sub>}:  

-   s<sub>0</sub> = 290797
-   s<sub><var>k</var>+1</sub> = s<sub><var>k</var></sub><sup>2</sup> mod 50515093
-   t<sub><var>k</var></sub> = (s<sub><var>k</var></sub> mod 64) + 1

Starting from the initial configuration (t<sub>0</sub>, t<sub>1</sub>, …, t<sub>10</sub>), the final state becomes \[1, 3, 10, 24, 51, 75\].  
Starting from the initial configuration (t<sub>0</sub>, t<sub>1</sub>, …, t<sub>10 000 000</sub>), find the final state.  
Give as your answer the sum of the squares of the elements of the final state. For example, if the final state is \[1, 2, 3\] then 14 ( = 1<sup>2</sup> + 2<sup>2</sup> + 3<sup>2</sup>) is your answer.
