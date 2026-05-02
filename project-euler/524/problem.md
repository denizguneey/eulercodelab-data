# Problem 524: First Sort II

Consider the following algorithm for sorting a list:

-   1\. Starting from the beginning of the list, check each pair of adjacent elements in turn.
-   2\. If the elements are out of order:
    -   a. Move the smallest element of the pair at the beginning of the list.
    -   b. Restart the process from step 1.
-   3\. If all pairs are in order, stop.

For example, the list $\\{\\,4\\,1\\,3\\,2\\,\\}$ is sorted as follows:

-   $\\underline{4\\,1}\\,3\\,2$ ($4$ and $1$ are out of order so move $1$ to the front of the list)
-   $1\\,\\underline{4\\,3}\\,2$ ($4$ and $3$ are out of order so move $3$ to the front of the list)
-   $\\underline{3\\,1}\\,4\\,2$ ($3$ and $1$ are out of order so move $1$ to the front of the list)
-   $1\\,3\\,\\underline{4\\,2}$ ($4$ and $2$ are out of order so move $2$ to the front of the list)
-   $\\underline{2\\,1}\\,3\\,4$ ($2$ and $1$ are out of order so move $1$ to the front of the list)
-   $1\\,2\\,3\\,4$ (The list is now sorted)

Let $F(L)$ be the number of times step 2a is executed to sort list $L$. For example, $F(\\{\\,4\\,1\\,3\\,2\\,\\}) = 5$.

We can list all permutations $P$ of the integers $\\{1, 2, \\dots, n\\}$ in **lexicographical order**, and assign to each permutation an index $I\_n(P)$ from $1$ to $n!$ corresponding to its position in the list.

Let $Q(n, k) = \\min(I\_n(P))$ for $F(P) = k$, the index of the first permutation requiring exactly $k$ steps to sort with First Sort. If there is no permutation for which $F(P) = k$, then $Q(n, k)$ is undefined.

For $n = 4$ we have:

<table border="1" style="text-align:left;"><tbody><tr><th><var>P</var></th><th><var>I</var><sub>4</sub>(<var>P</var>)</th><th><var>F</var>(<var>P</var>)</th><th></th></tr><tr><td>{1, 2, 3, 4}</td><td>1</td><td>0</td><td>Q(4, 0) = 1</td></tr><tr><td>{1, 2, 4, 3}</td><td>2</td><td>4</td><td>Q(4, 4) = 2</td></tr><tr><td>{1, 3, 2, 4}</td><td>3</td><td>2</td><td>Q(4, 2) = 3</td></tr><tr><td>{1, 3, 4, 2}</td><td>4</td><td>2</td><td></td></tr><tr><td>{1, 4, 2, 3}</td><td>5</td><td>6</td><td>Q(4, 6) = 5</td></tr><tr><td>{1, 4, 3, 2}</td><td>6</td><td>4</td><td></td></tr><tr><td>{2, 1, 3, 4}</td><td>7</td><td>1</td><td>Q(4, 1) = 7</td></tr><tr><td>{2, 1, 4, 3}</td><td>8</td><td>5</td><td>Q(4, 5) = 8</td></tr><tr><td>{2, 3, 1, 4}</td><td>9</td><td>1</td><td></td></tr><tr><td>{2, 3, 4, 1}</td><td>10</td><td>1</td><td></td></tr><tr><td>{2, 4, 1, 3}</td><td>11</td><td>5</td><td></td></tr><tr><td>{2, 4, 3, 1}</td><td>12</td><td>3</td><td>Q(4, 3) = 12</td></tr><tr><td>{3, 1, 2, 4}</td><td>13</td><td>3</td><td></td></tr><tr><td>{3, 1, 4, 2}</td><td>14</td><td>3</td><td></td></tr><tr><td>{3, 2, 1, 4}</td><td>15</td><td>2</td><td></td></tr><tr><td>{3, 2, 4, 1}</td><td>16</td><td>2</td><td></td></tr><tr><td>{3, 4, 1, 2}</td><td>17</td><td>3</td><td></td></tr><tr><td>{3, 4, 2, 1}</td><td>18</td><td>2</td><td></td></tr><tr><td>{4, 1, 2, 3}</td><td>19</td><td>7</td><td>Q(4, 7) = 19</td></tr><tr><td>{4, 1, 3, 2}</td><td>20</td><td>5</td><td></td></tr><tr><td>{4, 2, 1, 3}</td><td>21</td><td>6</td><td></td></tr><tr><td>{4, 2, 3, 1}</td><td>22</td><td>4</td><td></td></tr><tr><td>{4, 3, 1, 2}</td><td>23</td><td>4</td><td></td></tr><tr><td>{4, 3, 2, 1}</td><td>24</td><td>3</td><td></td></tr></tbody></table>

Let $R(k) = \\min(Q(n, k))$ over all $n$ for which $Q(n, k)$ is defined.

Find $R(12^{12})$.
