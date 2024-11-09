# Bet until win all the money

## Problem

???+ question "Question"

    === "English"

        A has $1 and B has $10. They bet $1 each time, with both having a 50% chance of winning each bet.
        What's the probability that A will win all of B's money?

    === "中文"

        A有1块钱，B有10块钱，一次赌一块钱，每次双方赢的概率都是50%。问A能把B赢光的概率是多少？

## Tip

??? tip "Tip"

    === "English"

        Transition Probability Matrix

    === "中文"

        概率转移矩阵


## Solutions

### Solution1
??? success "Solution1: Analysis"

    === "English"

        First, let's simplify the problem a bit: there is a total of 11 dollars in the entire gambling game.
        The game ends when one person's money becomes 0: either A loses everything, at which point B has 11 dollars; or B loses everything, at which point A has 11 dollars.

        Let's define the probability of A winning when having $x$ dollars as $P(A=x) = p_{x}$, then according to the game rules:

        \begin{align*}
            p_{11} &= 1 \\
            p_{0} &= 0 \\
        \end{align*}

        **Since A's initial stake is 1 dollar, the probability we're looking for is $p_{1}$**

        According to the game rules, to reach state $A=1$, there's only one scenario: losing one round after $A=2$,
        Thus we get the following relationship:

        $$
            p_{1} = \frac{1}{2} \cdot p_{2}
        $$

        Similarly, to reach state $A=2$, there are two scenarios: winning one round from $A=1$ or losing one round from $A=3$. Therefore:

        $$
            p_{2} = \frac{1}{2} \cdot p_{1} + \frac{1}{2} \cdot p_{3} \\
        $$

        Following this pattern, we can derive these relationships:

        \begin{align*}
            p_{2} &= \frac{1}{2} \cdot p_{1} + \frac{1}{2} \cdot p_{3} \\
            p_{3} &= \frac{1}{2} \cdot p_{2} + \frac{1}{2} \cdot p_{4} \\
            \vdots \\
            p_{9} &= \frac{1}{2} \cdot p_{8} + \frac{1}{2} \cdot p_{10} \\
        \end{align*}

        Let's rearrange these formulas:

        \begin{align*}
            p_{0} &= 0 \\
            p_{1} - \frac{1}{2} \cdot p_{2} &= 0 \\
            -\frac{1}{2} \cdot p_{1} + p_{2} - \frac{1}{2} \cdot p_{3} &= 0 \\
            -\frac{1}{2} \cdot p_{2} + p_{3} - \frac{1}{2} \cdot p_{4} &= 0 \\
            \vdots \\
            -\frac{1}{2} \cdot p_{7}  + p_{8} - \frac{1}{2} \cdot p_{9} &= 0 \\
            -\frac{1}{2} \cdot p_{8}  + p_{9} - \frac{1}{2} \cdot p_{10} &= 0 \\
            p_{11} &= 1 \\
        \end{align*}

        These equations can be written in matrix form:

        \begin{equation*}
            \begin{bmatrix}
                1 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                0 & 1 & -1/2 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                0 & -1/2 & 1 & -1/2 & 0 & \cdots & 0 & 0 & 0 & 0\\
                \vdots & \vdots & \vdots &\vdots &\vdots & \cdots &\vdots &\vdots &\vdots &\vdots \\
                0 & 0 & 0 & 0 & 0 & \cdots  & -1/2 & 1 & -1/2 & 0 \\
                0 & 0 & 0 & 0 & 0 & \cdots  & 0 & 0 & 0 & 1  \\
            \end{bmatrix}
            \begin{bmatrix}
                p_{0} \\ p_{1} \\p_{2} \\ \vdots \\ p_{9} \\ p_{10} \\ p_{11}
            \end{bmatrix} =
            \begin{bmatrix}
                0 \\ 0 \\ 0 \\ \vdots \\ 0 \\ 0 \\ 1
            \end{bmatrix}
        \end{equation*}

        This can be written as:

        $$
            Ax = b
        $$

        Where,

        $$
            \begin{align*}
                A &= \begin{bmatrix}
                        1 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        0 & 1 & -1/2 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        0 & -1/2 & 1 & -1/2 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        \vdots & \vdots & \vdots &\vdots &\vdots & \cdots &\vdots &\vdots &\vdots &\vdots \\
                        0 & 0 & 0 & 0 & 0 & \cdots  & -1/2 & 1 & -1/2 & 0 \\
                        0 & 0 & 0 & 0 & 0 & \cdots  & 0 & 0 & 0 & 1  \\
                    \end{bmatrix} \\
                x &= \begin{bmatrix}
                    p_{0} & p_{1} & p_{2} & \cdots & p_{9} & p_{10} & p_{11}
                    \end{bmatrix}^{T} \\
                b &= \begin{bmatrix}
                    0 & 0 & 0 & \cdots & 0 & 0 & 1
                \end{bmatrix}^{T}
            \end{align*}
        $$

        Using $X=A^{-1}B$, we solve for $x$:

        ??? tip "More precise matrix calculations"

            Here we can use `sympy` for more precise matrix calculations:

            ```python
            from sympy import Rational
            from sympy.matrices import Matrix


            def solve():
                matrix = [[0]*12 for _ in range(12)]
                # matrix rows: p0, p1
                matrix[0][0] = 1
                matrix[1][1], matrix[1][2] = 1, Rational(-1, 2)
                # matrix rows: p2~p10
                for i in range(2, 11):
                    matrix[i][i-1:i+2] = Rational(-1, 2), 1, Rational(-1, 2)
                # matrix rows: p11
                matrix[11][-1] = 1

                A = Matrix(matrix)
                b = Matrix([0] * 11 + [1])

                return A.inv() * b
            ```

            The running result is:

            ```
            Matrix([[0, 1/11, 2/11, 3/11, 4/11, 5/11, 6/11, 7/11, 8/11, 9/11, 10/11, 1]])
            ```

        $$
            x = [0, 1/11, 2/11, 3/11, 4/11, 5/11, 6/11, 7/11, 8/11, 9/11, 10/11, 1]^T
        $$

        Therefore,

        $$
            p_{1} = \frac{1}{11} \approx 0.09090909090909091
        $$

        So the probability of A winning all of B's money is $\frac{1}{11}$

    === "中文"

        首先让我们稍微简化一下问题：整个赌局从开始到结束，总共就是这 11 块钱。
        结束的标志的就是其中一个人的钱变为 0：要么 A 输光，此时 B 的钱是 11 块；要么 B 输光，此时 A 的钱是 11 块。

        设事件即 A 拥有$x$块钱时获胜的概率为$P(A=x) = p_{x}$，那么根据游戏规则有：

        \begin{align*}
            p_{11} &= 1 \\
            p_{0} &= 0 \\
        \end{align*}

        **因为 A 的初始赌资是 1 块钱，所以我们要求的概率就是$p_{1}$**。

        根据游戏规则得到$A=1$的状态只有一种情况：$A=2$后输一局，
        由此得到下面的关系：

        $$
            p_{1} = \frac{1}{2} \cdot p_{2}
        $$

        类似的，得到$A=2$的状态有两种种情况：$A=1$后赢一局或$A=3$后输一局。据此得：

        $$
            p_{2} = \frac{1}{2} \cdot p_{1} + \frac{1}{2} \cdot p_{3} \\
        $$

        以此类推，可以得到下述关系：

        \begin{align*}
            p_{2} &= \frac{1}{2} \cdot p_{1} + \frac{1}{2} \cdot p_{3} \\
            p_{3} &= \frac{1}{2} \cdot p_{2} + \frac{1}{2} \cdot p_{4} \\
            \vdots \\
            p_{9} &= \frac{1}{2} \cdot p_{8} + \frac{1}{2} \cdot p_{10} \\
        \end{align*}

        我们将上面的一系列公式整理一下，得到：

        \begin{align*}
            p_{0} &= 0 \\
            p_{1} - \frac{1}{2} \cdot p_{2} &= 0 \\
            -\frac{1}{2} \cdot p_{1} + p_{2} - \frac{1}{2} \cdot p_{3} &= 0 \\
            -\frac{1}{2} \cdot p_{2} + p_{3} - \frac{1}{2} \cdot p_{4} &= 0 \\
            \vdots \\
            -\frac{1}{2} \cdot p_{7}  + p_{8} - \frac{1}{2} \cdot p_{9} &= 0 \\
            -\frac{1}{2} \cdot p_{8}  + p_{9} - \frac{1}{2} \cdot p_{10} &= 0 \\
            p_{11} &= 1 \\
        \end{align*}

        那么上述方程式可以写成下面的形式：

        \begin{equation*}
            \begin{bmatrix}
                1 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                0 & 1 & -1/2 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                0 & -1/2 & 1 & -1/2 & 0 & \cdots & 0 & 0 & 0 & 0\\
                \vdots & \vdots & \vdots &\vdots &\vdots & \cdots &\vdots &\vdots &\vdots &\vdots \\
                0 & 0 & 0 & 0 & 0 & \cdots  & -1/2 & 1 & -1/2 & 0 \\
                0 & 0 & 0 & 0 & 0 & \cdots  & 0 & 0 & 0 & 1  \\
            \end{bmatrix}
            \begin{bmatrix}
                p_{0} \\ p_{1} \\p_{2} \\ \vdots \\ p_{9} \\ p_{10} \\ p_{11}
            \end{bmatrix} =
            \begin{bmatrix}
                0 \\ 0 \\ 0 \\ \vdots \\ 0 \\ 0 \\ 1
            \end{bmatrix}
        \end{equation*}

        上式可以写为：

        $$
            Ax = b
        $$

        其中，

        $$
            \begin{align*}
                A &= \begin{bmatrix}
                        1 & 0 & 0 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        0 & 1 & -1/2 & 0 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        0 & -1/2 & 1 & -1/2 & 0 & \cdots & 0 & 0 & 0 & 0\\
                        \vdots & \vdots & \vdots &\vdots &\vdots & \cdots &\vdots &\vdots &\vdots &\vdots \\
                        0 & 0 & 0 & 0 & 0 & \cdots  & -1/2 & 1 & -1/2 & 0 \\
                        0 & 0 & 0 & 0 & 0 & \cdots  & 0 & 0 & 0 & 1  \\
                    \end{bmatrix} \\
                x &= \begin{bmatrix}
                    p_{0} & p_{1} & p_{2} & \cdots & p_{9} & p_{10} & p_{11}
                    \end{bmatrix}^{T} \\
                b &= \begin{bmatrix}
                    0 & 0 & 0 & \cdots & 0 & 0 & 1
                \end{bmatrix}^{T}
            \end{align*}
        $$

        根据$X=A^{-1}B$, 求解得到$x$:

        ??? tip "更精确的矩阵运算"

            这里我们可以用`sympy`来进行更精确的矩阵运算：

            ```python
            from sympy import Rational
            from sympy.matrices import Matrix


            def solve():
                matrix = [[0]*12 for _ in range(12)]
                # matrix rows: p0, p1
                matrix[0][0] = 1
                matrix[1][1], matrix[1][2] = 1, Rational(-1, 2)
                # matrix rows: p2~p10
                for i in range(2, 11):
                    matrix[i][i-1:i+2] = Rational(-1, 2), 1, Rational(-1, 2)
                # matrix rows: p11
                matrix[11][-1] = 1

                A = Matrix(matrix)
                b = Matrix([0] * 11 + [1])

                return A.inv() * b
            ```

            运行返回结果为：

            ```
            Matrix([[0, 1/11, 2/11, 3/11, 4/11, 5/11, 6/11, 7/11, 8/11, 9/11, 10/11, 1]])
            ```

        $$
            x = [0, 1/11, 2/11, 3/11, 4/11, 5/11, 6/11, 7/11, 8/11, 9/11, 10/11, 1]^T
        $$

        因此，

        $$
            p_{1} = \frac{1}{11} \approx 0.09090909090909091
        $$

        所以 A 将 B 赢光的概率为$\frac{1}{11}$


[//]: # (### Solution2)

[//]: # (??? success "Solution2: Analysis")

[//]: # ()
[//]: # (    === "English")

[//]: # ()
[//]: # (        TBD)

[//]: # ()
[//]: # (    === "中文")

[//]: # ()
[//]: # (        带吸收壁的随机游走 OR 赌徒毁灭理论 OR 鞅论性质？)



### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        We can directly simulate the process of the gambling game to calculate the numerical solution to this problem:

        ```python exec="true" source="material-block" session="misc-2"
        --8<-- "docs/misc/snippet/2_bet_until_win.py:solution2"
        ```


    === "中文"

        我们可以直接模拟赌博游戏的过程来算出该问题的数值解：

        ```python exec="true" source="material-block" session="misc-2"
        --8<-- "docs/misc/snippet/2_bet_until_win.py:solution2"
        ```
