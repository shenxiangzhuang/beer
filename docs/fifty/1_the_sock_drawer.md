# The Sock Drawer

## Problem

???+ question "Question"

    === "English"

        A drawer contains red socks and black socks. When two socks are drawn at random,
        the probability that both are red is $\frac{1}{2}$

        (a) How small can the number of socks in the drawer be?

        (b) How small if the number of black socks is even?

    === "中文"

        一个抽屉里装有红袜子和黑袜子。
        当随机抽取两只袜子时，两只袜子都是红色的概率为$\frac{1}{2}$

        (a) 抽屉里的袜子数量最少可以是多少？

        (b) 如果黑袜子的数量是偶数，最少可以是多少？


## Tip

??? tip "Tip"

    === "English"

        Use probability equations to solve for radicals, Pell's equation

    === "中文"

        概率等式用于根式求解，Pell方程


## Solutions

### Solution1: Analysis
??? success "Solution1: Analysis"

    === "English"

        Let the number of red socks be denoted as $R \in \mathbb{Z}^{+}$,
        and the total number of socks be denoted as $N \in \mathbb{Z}^{+}$, where $N > R$.
        The probability of randomly picking a red sock on the first draw is $\frac{R}{N}$,
        and the probability of picking another red sock after picking a red sock on the first draw is $\frac{R-1}{N-1}$.
        Therefore, we have:

        $$\frac{1}{2} = \frac{R}{N}\frac{R-1}{N-1}$$

        Simplifying this equation, we get:

        $$N^2 - N + 2R(R-1) = 0$$

        Since our goal is to find the minimum value of $N$, combining the above conditions,
        the original problem can be formulated as the following integer programming problem:

        $$
        \begin{align*}
        \text{minimize} \quad & N \\
        \text{subject to} \quad & R \in \mathbb{Z}^{+} \\
        & N \in \mathbb{Z}^{+} \\
        & N > R \\
        & N^2 - N + 2R(1-R) = 0
        \end{align*}
        $$

        As for the canonical solution to this integer programming problem...
        I'm not quite familiar with it (feel free to submit a pull request to supplement it).
        Here, we'll use a relatively simple approach.

        Based on $N^2 - N + 2R(1-R) = 0$, since our goal is to find $N$,
        we can treat it as an unknown and use the quadratic formula to derive the corresponding values.
        Therefore, we have:

        $$N = \frac{1 \pm \sqrt{1 - 8R(1-R)}}{2}$$

        Considering the conditions that $N$ and $R$ are both positive integers, we can calculate:

        $$N = \frac{1 + \sqrt{1 - 8R(1-R)}}{2}$$

        And it must hold that $\sqrt{1 - 8R(1-R)}$ is an odd number, which requires $1 - 8R(1-R)$ to be a perfect square.

        We can find values that satisfy these conditions through an iterative approach:

        ```python
        --8<-- "docs/fifty/snippet/1_the_sock_drawer.py:solution1"
        ```

        Running the above code gives us:

        ```
        R = 3, N = 4, B = N - R = 1
        R = 15, N = 21, B = N - R = 6
        ```

        Obtaining the final answers::

        (a): At least 4 socks are needed (3 red and 1 black), in this case, we have
             $\frac{R}{N}\frac{R-1}{N-1} = \frac{3}{4}\frac{2}{3} = \frac{1}{2}$

        (b): At least 21 socks are needed (15 red and 6 black), in this case, we have
             $\frac{R}{N}\frac{R-1}{N-1} = \frac{15}{21}\frac{14}{20} = \frac{1}{2}$


    === "中文"

        记红色袜子的个数为$R \in \mathbb{Z}^{+}$，袜子总数为$N \in \mathbb{Z}^{+}$, 且$N > R$，
        那么第一次随机拿到红袜子的概率$\frac{R}{N}$，在第一次拿到红袜子后第二次又拿到红色的概率为$\frac{R-1}{N-1}$，由此得

        $$\frac{1}{2} = \frac{R}{N}\frac{R-1}{N-1}$$

        化简得，

        $$N^2 - N + 2R(R-1) = 0$$

        因为我们的目的是求$N$的最小值，综合以上条件，原问题可以整理为如下整数规划问题

        $$
        \begin{align*}
        \text{minimize} \quad & N \\
        \text{subject to} \quad & R \in \mathbb{Z}^{+} \\
        & N \in \mathbb{Z}^{+} \\
        & N > R \\
        & N^2 - N + 2R(1-R) = 0
        \end{align*}
        $$

        至于这个整数规划问题的规范解法...我还不太会(欢迎提PR补充). 这里采用一种相对简单的解法。

        根据$N^2 - N + 2R(1-R) = 0$，因为我们的目的是求$N$，这里可以将其看作未知数，然后用求根公式来接出对应的值，所以有

        $$N = \frac{1 \pm \sqrt{1 - 8R(1-R)}}{2}$$

        根据$N$, $R$均为正整数的条件，可以算出

        $$N = \frac{1 + \sqrt{1 - 8R(1-R)}}{2}$$

        且必须有$\sqrt{1 - 8R(1-R)}$为奇数，这就要求$1 - 8R(1-R)$必须为平方数。

        可以通过遍历的方法来求出找出符合条件的值:

        ```python
        --8<-- "docs/fifty/snippet/1_the_sock_drawer.py:solution1"
        ```

        运行上述代码可以得到:
        ```
        R = 3, N = 4, B = N - R = 1
        R = 15, N = 21, B = N - R = 6
        ```

        得到最终答案:

        (a): 最少有4只袜子(3红1黑)，此时有$\frac{R}{N}\frac{R-1}{N-1} = \frac{3}{4}\frac{2}{3} = \frac{1}{2}$

        (b): 最少有21只袜子(15红6黑)，此时有$\frac{R}{N}\frac{R-1}{N-1} = \frac{15}{21}\frac{14}{20} = \frac{1}{2}$


### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        The above method is to analyze the simplified problem first and then solve it. 
        We can also make full use of the powerful computing power of the computer to directly solve this problem. 
        Let’s take a look at the "violent aesthetics" of computers!

        ```python
        --8<-- "docs/fifty/snippet/1_the_sock_drawer.py:solution2"
        ```

        Running the above code gives us:

        ```
        R = 3, N = 4, B = N - R = 1
        R = 15, N = 21, B = N - R = 6
        ```

        Obtaining the final answers::

        (a): At least 4 socks are needed (3 red and 1 black), in this case, we have
             $\frac{R}{N}\frac{R-1}{N-1} = \frac{3}{4}\frac{2}{3} = \frac{1}{2}$

        (b): At least 21 socks are needed (15 red and 6 black), in this case, we have
             $\frac{R}{N}\frac{R-1}{N-1} = \frac{15}{21}\frac{14}{20} = \frac{1}{2}$


    === "中文"

        上面的方法是先分析简化问题之后再求解，我们也可以充分利用计算机强大的计算能力来直接求解本问题。
        让我们一起来看下计算机的“暴力美学”吧!

        ```python
        --8<-- "docs/fifty/snippet/1_the_sock_drawer.py:solution2"
        ```

        运行上述代码同样可以得到:
        ```
        R = 3, N = 4, B = N - R = 1
        R = 15, N = 21, B = N - R = 6
        ```

        得到相同的答案:

        (a): 最少有4只袜子(3红1黑)，此时有$\frac{R}{N}\frac{R-1}{N-1} = \frac{3}{4}\frac{2}{3} = \frac{1}{2}$

        (b): 最少有21只袜子(15红6黑)，此时有$\frac{R}{N}\frac{R-1}{N-1} = \frac{15}{21}\frac{14}{20} = \frac{1}{2}$
