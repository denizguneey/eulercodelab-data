# Problem 124: Ordered Radicals

The radical of $n$, $\\mathrm{rad}(n)$, is the product of the distinct prime factors of $n$. For example, $504 = 2^3 \\times 3^2 \\times 7$, so $\\mathrm{rad}(504) = 2 \\times 3 \\times 7 = 42$.

If we calculate $\\mathrm{rad}(n)$ for $1 \\le n \\le 10$, then sort them on $\\mathrm{rad}(n)$, and sorting on $n$ if the radical values are equal, we get:

<table class="center"><tbody><tr><th colspan="2">Unsorted</th><td class="w25">&nbsp;</td><th colspan="3">Sorted</th></tr><tr><th class="w50"><i>n</i></th><th class="w50">rad(<i>n</i>)</th><td>&nbsp;</td><th class="w50"><i>n</i></th><th class="w50">rad(<i>n</i>)</th><th class="w50">k</th></tr><tr><td>1</td><td>1</td><td>&nbsp;</td><td>1</td><td>1</td><td>1</td></tr><tr><td>2</td><td>2</td><td>&nbsp;</td><td>2</td><td>2</td><td>2</td></tr><tr><td>3</td><td>3</td><td>&nbsp;</td><td>4</td><td>2</td><td>3</td></tr><tr><td>4</td><td>2</td><td>&nbsp;</td><td>8</td><td>2</td><td>4</td></tr><tr><td>5</td><td>5</td><td>&nbsp;</td><td>3</td><td>3</td><td>5</td></tr><tr><td>6</td><td>6</td><td>&nbsp;</td><td>9</td><td>3</td><td>6</td></tr><tr><td>7</td><td>7</td><td>&nbsp;</td><td>5</td><td>5</td><td>7</td></tr><tr><td>8</td><td>2</td><td>&nbsp;</td><td>6</td><td>6</td><td>8</td></tr><tr><td>9</td><td>3</td><td>&nbsp;</td><td>7</td><td>7</td><td>9</td></tr><tr><td>10</td><td>10</td><td>&nbsp;</td><td>10</td><td>10</td><td>10</td></tr></tbody></table>

Let $E(k)$ be the $k$-th element in the sorted $n$ column; for example, $E(4) = 8$ and $E(6) = 9$.

If $\\mathrm{rad}(n)$ is sorted for $1 \\le n \\le 100000$, find $E(10000)$.
