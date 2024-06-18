# 生育政策与男女比例 (Fertility Policy)


## Problem

???+ question "Question"

    === "English"

        If a family stops having children after giving birth to a boy, and continues to have children after giving birth to a girl until a boy is born, the question is: What will the gender ratio be in this place?

    === "中文"

        如果一个家庭生下男孩就不再生孩子，如果是女孩子就继续生，直到生出男孩为止，问：这个地方的男女比例会是多少？


## Tip

??? tip "Tip"

    === "English"

        There are many solutions, which can be approached from the perspectives of expectation,
        geometric distribution, probability, biology, etc.

    === "中文"

        很多种解法，可以从期望、几何分布、概率，生物学等角度入手。

## Solutions

### Solution1

??? success "Solution1"

    === "English"

        Since there is only one boy in a family, asking about the ratio of boys to girls is equivalent to asking the **average number of girls per family**.

        Let the number of girls in a family be $X$, and the **average number of girls per family** be $E(X)$, and the problem is transformed into solving $1:E(X)$.

        Since the probability of having a boy and a girl is equal, the distribution of X is as follows:

        <div align="center">

        | X | Sequence                     | Probability       |
        |---|------------------------------|-------------------|
        | 0 | Male                         | $\frac{1}{2}$     |
        | 1 | Female, Male                 | $(\frac{1}{2})^2$ |
        | 2 | Female, Female, Male         | $(\frac{1}{2})^3$ |
        | 3 | Female, Female, Female, Male | $(\frac{1}{2})^4$ |

        </div>

        According to the definition of expectation, $E(X)$ satisfies the following equation:

        $$
        \begin{align}
            E(X) &= \frac{1}{2} \times 0 + (\frac{1}{2})^2 \times 1 + (\frac{1}{2})^3 \times 2 + \cdots \\
                 &= (\frac{1}{2})^2 \times 1 + (\frac{1}{2})^3 \times 2 + \cdots
        \end{align}
        $$

        Therefore,

        $$
            2E(X) = (\frac{1}{2})^1 \times 1 + (\frac{1}{2})^2 \times 2 + \cdots
        $$

        Subtracting the two equations, we get:

        $$
        \begin{align}
            E(X) &= (\frac{1}{2})^1 \times 1 + (\frac{1}{2})^2 \times 1 + \cdots \\
                 &= lim_{n\to\infty} \frac{\frac{1}{2}(1-(\frac{1}{2})^n)}{1-\frac{1}{2}} \\
                 &= \frac{\frac{1}{2} \times 1}{\frac{1}{2}} \\
                 &= 1
        \end{align}
        $$

    === "中文"

        因为一个家庭有且仅有一个男孩，所以问男女比例等价于问**平均每个家庭女孩的数量**。
        设家庭中女孩的数量为$X$, **平均每个家庭女孩的数量**则为$E(X)$，问题转化为求解$1:E(X)$。

        由于生男孩和生女孩的概率相等，X的分布如下：

        <div align="center">

        | X | Sequence | Probability       |
        |---|----------|-------------------|
        | 0 | 男        | $\frac{1}{2}$     |
        | 1 | 女男       | $(\frac{1}{2})^2$ |
        | 2 | 女女男      | $(\frac{1}{2})^3$ |
        | 3 | 女女女男     | $(\frac{1}{2})^4$ |
        | ...| ...        | ... |

        </div>

        根据期望的定义, $E(X)$满足下式：

        $$
        \begin{align}
            E(X) &= \frac{1}{2} \times 0 + (\frac{1}{2})^2 \times 1 + (\frac{1}{2})^3 \times 2 + \cdots \\
                 &= (\frac{1}{2})^2 \times 1 + (\frac{1}{2})^3 \times 2 + \cdots
        \end{align}
        $$

        因此,

        $$
            2E(X) = (\frac{1}{2})^1 \times 1 + (\frac{1}{2})^2 \times 2 + \cdots
        $$

        两式相减得到：

        $$
        \begin{align}
            E(X) &= (\frac{1}{2})^1 \times 1 + (\frac{1}{2})^2 \times 1 + \cdots \\
                 &= lim_{n\to\infty} \frac{\frac{1}{2}(1-(\frac{1}{2})^n)}{1-\frac{1}{2}} \\
                 &= \frac{\frac{1}{2} \times 1}{\frac{1}{2}} \\
                 &= 1
        \end{align}
        $$

### Solution2

??? success "Solution2"

    === "English"

        Define that when a family gives birth to a boy, the total number of children in the current family is $X$, and the number of girls is $Y$, then $X$ meets the definition of geometric distribution (strictly speaking, it should be shifted geometric distribution), which is the probability distribution of the number of first successes in the Bernoulli test, and $p=\frac{1}{2}$. According to the expected formula of geometric distribution, we have:

        $$
        E(X) = \frac{1}{p} = 2
        $$

        Because the number of boys is 1, the number of girls is $Y=X-1$, so we have:

        $$
        E(Y) = E(X-1) = E(X) - 1 = 1
        $$

        That is, there is an average of 1 girl in each family, so the ratio of boys to girls is 1:1.

    === "中文"

        定义一个家庭生下男孩时，当前家庭孩子的总数量为$X$, 女孩数量为$Y$, 则$X$符合几何分布(严格来说应该是shifted geometric distribution)的定义，
        即为Bernoulli试验中第一次成功的次数的概率分布, 此时$p=\frac{1}{2}$。
        根据几何分布的期望公式，有:

        $$
            E(X) = \frac{1}{p} = 2
        $$
        因为男孩数量为1，所以女孩数量为$Y=X-1$，所以有:
        $$
            E(Y) = E(X-1) = E(X) - 1 = 1
        $$
        即每个家庭平均有1个女孩，所以男女比例为1:1。


### Solution3

??? success "Solution3"

    === "English"

        Consider a birth process as an event, let event A be the birth of a boy, and event B be the birth of a girl.
        Then: $P(A) = \frac{1}{2}$, $P(B) = \frac{1}{2}$.
        Regardless of the birth policy,
        it is ultimately a series of independent birth events,
        so the final male-female ratio is 1:1.

    === "中文"

        把一次生育过程看作一个事件，设事件A为生男孩，事件B为生女孩。
        则有: $P(A) = \frac{1}{2}$, $P(B) = \frac{1}{2}$.
        无论生育政策如何，最终都是一系列相互独立的生育事件，所以最终的男女比例是1:1。


### TODO: Solution4: Simulation
