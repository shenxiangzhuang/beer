# Trials until first success

## Problem

???+ question "Question"

    === "English"

        On the average, how many times must a die be thrown until one gets a 6?

    === "中文"

        平均需要掷骰子多少次才能得到一个6点？


## Tip

??? tip "Tip"

    === "English"

        Geometric series

    === "中文"

        几何级数


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        Let's denote the number of tosses required as $T$. We can determine the probability distribution of $T$ and then calculate the expected value $E(T)$ based on this distribution.

        <div align="center">

        | T | Probability |
        |---|---|
        | 1 | $\frac{1}{6}$ |
        | 2 | $\frac{1}{6} \cdot (\frac{5}{6})$ |
        | 3 | $\frac{1}{6} \cdot (\frac{5}{6})^2$ |
        | ... | ... |
        | t | $\frac{1}{6} \cdot (\frac{5}{6})^{t-1}$ |

        </div>

        Therefore, we have

        $$E(T) = \sum_{t=1}^{\infty}{t \cdot \frac{1}{6} \cdot (\frac{5}{6})^{t-1}}$$

        From

        $$\frac{5}{6}E(T) = \sum_{t=1}^{\infty}{t \cdot \frac{1}{6} \cdot (\frac{5}{6})^{t}}$$

        we can deduce that

        $$E(T) - \frac{5}{6}E(T) = \frac{1}{6}E(T) = \frac{1}{6}(1 + \sum_{i=1}^{\infty}{(\frac{5}{6})^i}) = 1$$

        Hence,

        $$E(T) = 6$$


    === "中文"

        记问题需要的投掷次数为$T$，那么可以得到如下$T$的概率分布，
        我们可以根据此概率分布求出最终的$E(T)$

        <div align="center">

        | T | Probability |
        |---|---|
        | 1 | $\frac{1}{6}$ |
        | 2 | $\frac{1}{6} \cdot (\frac{5}{6})$ |
        | 3 | $\frac{1}{6} \cdot (\frac{5}{6})^2$ |
        | ... | ... |
        | t | $\frac{1}{6} \cdot (\frac{5}{6})^{t-1}$ |

        </div>

        所以有

        $$E(T) = \sum_{t=1}^{\infty}{t \cdot \frac{1}{6} \cdot (\frac{5}{6})^{t-1}}$$

        由

        $$\frac{5}{6}E(T) = \sum_{t=1}^{\infty}{t \cdot \frac{1}{6} \cdot (\frac{5}{6})^{t}}$$

        得

        $$E(T) - \frac{5}{6}E(T) = \frac{1}{6}E(T) = \frac{1}{6}(1 + \sum_{i=1}^{\infty}{(\frac{5}{6})^i}) = 1$$

        $$E(T) = 6$$


### Solution2: Elegant Analysis

??? success "Solution2: Elegant Analysis"

    === "English"
        This extremely elegant problem-solving idea comes from the reference answers in the book.

        When the first toss is a failure,
        the mean number of tosses required is $1 + E(T)$,
        and when the first toss is a success, the mean number is 1. Then

        $$E(T) = \frac{5}{6} \cdot (1 + E(T)) + \frac{1}{6} \cdot 1$$

        $$E(T) = 6$$

    === "中文"

        这个极其优雅的解题思路来自书的参考答案。

        当第一次投掷失败时，所需的平均投掷次数为$1 + E(T)$；
        当第一次投掷成功时，所需的平均投掷次数为1。因此，

        $$E(T) = \frac{5}{6} \cdot (1 + E(T)) + \frac{1}{6} \cdot 1$$

        $$E(T) = 6$$


### Solution3: Simulation

??? success "Solution3: Simulation"

    === "English"

        We can approximate the average number of times it takes to roll a dice to get a 6
        by simulating the process of rolling a dice.

        ```python exec="true" source="material-block" session="fifty-4"
        --8<-- "docs/fifty/snippet/4_first_success.py:solution3"
        ```

    === "中文"

        可以通过模拟掷骰子的过程来近似得到平均需要掷骰子多少次才能得到一个6点。

        ```python exec="true" source="material-block" session="fifty-4"
        --8<-- "docs/fifty/snippet/4_first_success.py:solution3"
        ```
