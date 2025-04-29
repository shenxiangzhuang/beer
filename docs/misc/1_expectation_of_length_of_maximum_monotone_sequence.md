# Expectation of Length of Maximum Monotone Sequence

## Problem

???+ question "Question"

    === "English"
        Keep picking points uniformly randomly on [0,1].
        If your current sequence is a monotonically increasing sequence, continue.
        What is the expected length of this monotonous sequence?


        The formal definition of the current problem is as follows:
        Remark: $\mathbb{N} = \{ 1,2,\dots \}$.

        Consider the space $X = [0,1]^\mathbb{N}$, where a probability measure $p$ is defined by selecting a sequence of points uniformly from the interval $[0,1]$. And given function $f: X \rightarrow [0,1]$ as:

        $$
        f(\gamma) = \sup \{
            n \in \mathbb{N} \mid \gamma_i < \gamma_{i+1}, \forall i < n
        \}
        $$

        Calculate $E[f(X)]$.

    === "中文"

        在[0,1]上均匀随机的一直取点，如果你当前的序列是一个单调递增序列就继续，请问这个单调序列的期望长度是多少？


        当前问题的形式化定义如下:
        备注：$\mathbb{N} = \{ 1,2,\dots \}$.

        设空间$X = [0,1]^\mathbb{N}$，其中概率测度$p$通过从区间$[0,1]$中均匀选择一个序列的点来定义。给定函数$f: X \rightarrow [0,1]$如下：

        $$
        f(\gamma) = \sup \{
            n \in \mathbb{N} \mid \gamma_i < \gamma_{i+1}, \forall i < n
        \}
        $$

        计算$E[f(X)]$。

## Tip

??? tip "Tip"

    === "English"

        Consider the probability that the monotone growing sequence stops at $n$.

    === "中文"

        考虑单调增长序列在$n$处停止的概率。


## Solutions

### Solution1
??? success "Solution1: Analysis"

    === "English"

        For $n\in \mathbb{N}$,
        consider set $C_n = \{
            \gamma \in X \mid f(\gamma) \ge n
        \}$,
        and $A_n = \{
            \gamma \in X \mid f(\gamma) = n
        \}$.
        And $A_\infty = \{
            \gamma \in X \mid f(\gamma) = \infty
        \}$.

        It is obvious that $C_1 \supset C_2 \supset \dots \supset C_\infty$
        and $C_1 = X$.
        It is also obvious that all $C_n$ are measurable,
        as it can be written as countable union of measurable sets.

        Furthermore, sets in $\{A_n \mid n\in\mathbb{N}\}\cup\{A_\infty\}$
        are mutually disjoint
        and $X = C_\infty\cup\bigcup_{n\in\mathbb{N}} C_n$.
        Also, $A_n = C_n \setminus C_{n+1}$. So $p(A_n) = p(C_n) - p(C_{n+1})$.

        We can see that, $p(C_n)$ can be easily calculated
        as it is the probability that the first $n$ points are in increasing order.
        Thus,

        $$
            \begin{align}
                p(C_n) &= p(\{
                    \gamma\in X \mid \gamma_1 < \gamma_2 < \dots < \gamma_n
                \}) \\
                &= \int_0^1 \int^1_{\gamma_1} \dots \int^1_{\gamma_{n-1}} d\gamma_n \dots d\gamma_2 d\gamma_1 \\
                &= \frac{1}{n!}.
            \end{align}
        $$

        And therefore, we can see that,
        $p(A_n) = \frac{1}{n!} - \frac{1}{(n+1)!}$.
        And

        $$
            \begin{align}
                p(A_\infty) &= 1 - p\left(
                    \bigcup_{n\in\mathbb{N}} A_n
                \right) \\
                &= 1 - \sum_{n\in\mathbb{N}} p(A_n) \\
                &= 1 - \sum_{n\in\mathbb{N}} \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
                \right) \\
                &= 0.
            \end{align}
        $$

        Finally, we can calculate $E[f(X)]$ as:

        $$
            \begin{align}
                E[f(X)] &= \infty \times p(A_\infty) + \sum_{n\in\mathbb{N}} n p(A_n) \\
                &= 0 + \sum_{n\in\mathbb{N}} n \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
                \right).
            \end{align}
        $$

        By Taylor expansion, we can see that

        $$
            \frac{d}{dx} \left(
                e^x - \frac{e^x -1}{x}
            \right) = \sum_{n\in\mathbb{N}} n \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
            \right) x^{n-1}.
        $$

        Therefore,

        $$
            \begin{align}
                E[f(X)] &= \frac{d}{dx} \left(
                    e^x - \frac{e^x -1}{x}
                \right) \Big|_{x=1} \\
                &= e - 1.
            \end{align}
        $$

    === "中文"

        对于 $n\in \mathbb{N}$，考虑集合 $C_n = \{
            \gamma \in X \mid f(\gamma) \ge n
        \}$，以及 $A_n = \{
            \gamma \in X \mid f(\gamma) = n
        \}$。再定义 $A_\infty = \{
            \gamma \in X \mid f(\gamma) = \infty
        \}$。

        显然 $C_1 \supset C_2 \supset \dots \supset C_\infty$ 并且 $C_1 = X$。
        同样显然，所有的 $C_n$ 都是可测集，因为它们可以表示为可测集的可数并集。

        此外，集合 $\{A_n \mid n\in\mathbb{N}\}\cup\{A_\infty\}$ 是互不相交的，
        并且 $X = C_\infty\cup\bigcup_{n\in\mathbb{N}} C_n$。
        同时，$A_n = C_n \setminus C_{n+1}$，所以 $p(A_n) = p(C_n) - p(C_{n+1})$。

        我们可以看到，$p(C_n)$ 可以很容易地计算出来，
        因为它是前 $n$ 个点按递增顺序排列的概率。因此，

        $$
            \begin{align}
                p(C_n) &= p(\{
                    \gamma\in X \mid \gamma_1 < \gamma_2 < \dots < \gamma_n
                \}) \\
                &= \int_0^1 \int^1_{\gamma_1} \dots \int^1_{\gamma_{n-1}} d\gamma_n \dots d\gamma_2 d\gamma_1 \\
                &= \frac{1}{n!}。
            \end{align}
        $$

        因此，我们可以看到，$p(A_n) = \frac{1}{n!} - \frac{1}{(n+1)!}$。接下来

        $$
            \begin{align}
                p(A_\infty) &= 1 - p\left(
                    \bigcup_{n\in\mathbb{N}} A_n
                \right) \\
                &= 1 - \sum_{n\in\mathbb{N}} p(A_n) \\
                &= 1 - \sum_{n\in\mathbb{N}} \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
                \right) \\
                &= 0。
            \end{align}
        $$

        最后，我们可以计算 $E[f(X)]$ 如下：

        $$
            \begin{align}
                E[f(X)] &= \infty \times p(A_\infty) + \sum_{n\in\mathbb{N}} n p(A_n) \\
                &= 0 + \sum_{n\in\mathbb{N}} n \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
                \right)。
            \end{align}
        $$

        通过泰勒展开，我们可以看到

        $$
            \frac{d}{dx} \left(
                e^x - \frac{e^x -1}{x}
            \right) = \sum_{n\in\mathbb{N}} n \left(
                    \frac{1}{n!} - \frac{1}{(n+1)!}
            \right) x^{n-1}。
        $$

        因此，

        $$
            \begin{align}
                E[f(X)] &= \frac{d}{dx} \left(
                    e^x - \frac{e^x -1}{x}
                \right) \Big|_{x=1} \\
                &= e - 1。
            \end{align}
        $$


### Solution2

> This solution is authored by [@yuanhang](https://yuanhang0.github.io/).

??? success "Solution2: Analysis"

    === "English"

        Define the indicator variable $X_i$:

        - $X_i=1$: The sequence remains strictly increasing before the $i$-th element
          - $X_i=0$: The sequence is no longer strictly increasing before the $i$-th element

        Then the sequence length $f$ as the number of $X_i$ that are 1, i.e., the number of elements before the sequence stops being strictly increasing.
        Therefore, the sequence length $f$ can be expressed as the sum of these indicator variables:

        $$
            f(X) = \sum_{i}^{\infty}X_i
        $$

        According to the linearity of expectation, we have:

        $$
            E[f(X)] = E \left[ \sum_{i}^{\infty}X_i \right] = \sum_{i}^{\infty}E[X_i]
        $$

        Now let's calculate $E[X_i]$. To ensure $E[X_i] = 1$, the sequence formed by all points before the $i$-th point must be strictly increasing.
        The probability of randomly selecting $i$ points in the interval $[0, 1]$ such that they form a strictly increasing sequence is $\frac{1}{i!}$:

        $$
            E[X_i] = \frac{1}{i!}
        $$

        Adding up all $E[X_i]$, we get:

        $$
            E[f(X)] = \sum_{i=1}^{\infty}\frac{1}{i!} = e - 1
        $$

    === "中文"

        定义指示变量$X_i$:

        - $X_i=1$: 序列在第$i$个元素之前保持单调递增
        - $X_i=0$: 序列在第$i$个元素之前不再保持单调递增


        那么序列长度$f$就是所有$X_i$为 1 的个数，即序列在停止前的元素数目。
        因此，序列长度$f$可以表示为这些指示变量的和：

        $$
            f(X) = \sum_{i}^{\infty}X_i
        $$

        根据期望值的线性性质，我们有：

        $$
            E[f(X)] = E \left[ \sum_{i}^{\infty}X_i \right] = \sum_{i}^{\infty}E[X_i]
        $$

        下面我们来计算$E[X_i]$, 要保证$E[X_i] = 1$，需要第$i$个点之前所有点形成的序列是单调递增的。
        在$[0, 1]$区间内随机取$i$个点，使其严格递增的概率是$\frac{1}{i!}$:

        $$
            E[X_i] = \frac{1}{i!}
        $$

        将所有$E[X_i]$相加，得到：

        $$
            E[f(X)] = \sum_{i=1}^{\infty}\frac{1}{i!} = e - 1
        $$


### Solution3: Simulation


??? success "Solution3: Simulation"

    === "English"

        We can directly simulate the process of taking points to
        find the mean of the length of the monotone sequence as the numerical solution to this problem:

        ```python exec="true" source="material-block" session="misc-1"
        --8<-- "docs/misc/snippet/1_monotone_sequence.py:solution"
        ```


    === "中文"

        我们可以直接模拟取点的过程来求出单调序列长度的均值作为该问题的数值解:

        ```python exec="true" source="material-block" session="misc-1"
        --8<-- "docs/misc/snippet/1_monotone_sequence.py:solution"
        ```
