# Curing the Compulsive Gambler

## Problem

???+ question "Question"

    === "English"

        Mr. Brown always bets a dollar on the number 13 at roulette against the
        advice of Kind Friend To help cure Mr Brown of playing roulette, Kind Frien(f
        always bets Brown $20 at even money that Brown will be behind at the end of
        36 plays. How is the cure working?

        (Most American roulette wheels have 38 equally likely numbers. If the
        player's number comes up, he is paid 35 times his stake and gets his original
        stake back; otherwise he loses his stake)

    === "中文"

        布朗先生总是不听好友的建议，在轮盘赌中押1美元在13号上。为了帮助布朗先生戒掉轮盘赌，好友总是以1:1的赔率和布朗先生打赌20美元，
        赌布朗先生在36次游戏结束后会亏钱。这个治疗方法效果如何？

        （大多数美国轮盘赌轮有38个等概率的数字。如果玩家押中的数字出现，他将获得35倍于赌注的赔付，并收回原始赌注；否则，他将损失赌注）


## Tip

??? tip "Tip"

    === "English"

        The core of the problem is to find out how Mr. Brown's expectation
        of winning changes after adding the bet with his friend. Since we are looking for expectation,
        we need to define the random variable first, then find the probability of its distribution,
        and finally find the expectation.

    === "中文"

        问题的核心是求加上和朋友的赌约之后，布朗先生赢钱期望的变化如何。
        既然是求期望，那么我们需要先定义随机变量，然后找出其分布的概率，最后求期望即可。


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        First, let's consider the situation without betting with a friend, where Mr. Brown plays roulette 36 times on his own.
        Let's denote Mr. Brown's expected winnings in this case as $R_1$, so his expected winnings are $E(R_1)$.
        To calculate $E(R_1)$, we first need to list the distribution of $R_1$, as follows:

        <div align="center">

        | Win Times | $R_1$ | Probability                                           |
        |-----------|-------|-------------------------------------------------------|
        | 0         | $-36$ | $(\frac{37}{38})^{36}$                                |
        | 1         | $0$   | $\binom{36}{1} (\frac{37}{38})^{35} (\frac{1}{38})^1$ |
        | 2         | $36$  | $\binom{36}{2} (\frac{37}{38})^{34} (\frac{1}{38})^2$ |
        | ...       | ...   | ...                                                   |

        </div>

        From this, we can calculate


        $$
        E(R_1) = \sum_{i=0}^{36}{(36(i-1)) \cdot \binom{36}{i} (\frac{37}{38})^{36-i}(\frac{1}{38})^i} ≈ -1.8947368421052684
        $$

        This means that without the bet with his friend, Mr. Brown would lose about $1.89 on average for every 36 games of roulette.

        Now let's consider how much Mr. Brown is expected to win when playing 36 games of roulette with the additional bet with his friend.

        ???+ tip "Bet Analysis"

            The bet essentially states that if Mr. Brown loses money after 36 games of roulette, he gives his friend an additional $20.
            Conversely, if Mr. Brown breaks even or wins money, his friend gives him $20.

            Based on the above analysis, Mr. Brown will only lose money overall if he loses all 36 games. If he wins even one game, he won't lose money, and if he wins 2 or more games, he'll make money.
            In other words, Mr. Brown will only have to pay his friend an extra $20 if he loses all 36 games. In all other cases, he will earn $20 from his friend.

        Let's denote Mr. Brown's expected winnings in this case as $R_2$, so his expected winnings are $E(R_2)$.
        To calculate $E(R_2)$, we first need to list the distribution of $R_2$, as follows:


        <div align="center">

        | Win Times | $R_1$ | Probability                                           |
        |-----------|-------|-------------------------------------------------------|
        | 0         | $-36 - 20$ | $(\frac{37}{38})^{36}$                                |
        | 1         | $0 + 20$   | $\binom{36}{1} (\frac{37}{38})^{35} (\frac{1}{38})^1$ |
        | 2         | $36 + 20$  | $\binom{36}{2} (\frac{37}{38})^{34} (\frac{1}{38})^2$ |
        | ...       | ...   | ...                                                   |

        </div>

        From this, we can calculate


        $$
        E(R_2) = (-36 - 20)\cdot \frac{37}{38})^{36} + \sum_{i=1}^{36}{(36(i-1) + 20) \cdot \binom{36}{i} (\frac{37}{38})^{36-i}(\frac{1}{38})^i} ≈ 2.7904190810856586
        $$

    === "中文"
        首先考虑不和朋友打赌时的情况，此时单独玩36次轮盘赌。
        记此时布朗先生赢钱的期望为$R_1$，那么布朗先生的预期赢钱数为$E(R_1)$,
        因为要求$E(R_1)$，所以我们先列出$R_1$的分布，如下：

        <div align="center">

        | Win Times | $R_1$ | Probability                                           |
        |-----------|-------|-------------------------------------------------------|
        | 0         | $-36$ | $(\frac{37}{38})^{36}$                                |
        | 1         | $0$   | $\binom{36}{1} (\frac{37}{38})^{35} (\frac{1}{38})^1$ |
        | 2         | $36$  | $\binom{36}{2} (\frac{37}{38})^{34} (\frac{1}{38})^2$ |
        | ...       | ...   | ...                                                   |

        </div>

        由此计算出


        $$
        E(R_1) = \sum_{i=0}^{36}{(36(i-1)) \cdot \binom{36}{i} (\frac{37}{38})^{36-i}(\frac{1}{38})^i} ≈ -1.8947368421052684
        $$

        也就是说，在没有和朋友的赌约下，布朗先生平均每36局轮盘赌大概要输约1.89美元。

        下面来考虑加上和朋友赌约的情况下，布朗先生玩36局轮盘赌的预期赢钱数是多少。

        ???+ tip "赌约分析"

            赌约内容简单来说就是如果布朗先生36局轮盘赌之后是输钱，那么布朗先生另外拿20美元给朋友；
            反之，如果布朗先生不输不赢或者赢钱了，那么朋友拿20美元给到布朗先生。

            根据上面的分析，布朗先生只有36局全输的情况下才会最终输钱，只要赢1局就能不输钱，赢2局或以上就能赢钱。
            也就是说，布朗先生只有在36局全输的情况下才会额外输给朋友20美元，其他情况下都会从朋友那里赚20美元。

        记此时布朗先生赢钱的期望为$R_2$，那么布朗先生的预期赢钱数为$E(R_2)$,
        因为要求$E(R_2)$，所以我们先列出$R_2$的分布, 如下:


        <div align="center">

        | Win Times | $R_1$ | Probability                                           |
        |-----------|-------|-------------------------------------------------------|
        | 0         | $-36 - 20$ | $(\frac{37}{38})^{36}$                                |
        | 1         | $0 + 20$   | $\binom{36}{1} (\frac{37}{38})^{35} (\frac{1}{38})^1$ |
        | 2         | $36 + 20$  | $\binom{36}{2} (\frac{37}{38})^{34} (\frac{1}{38})^2$ |
        | ...       | ...   | ...                                                   |

        </div>

        由此计算出


        $$
        E(R_2) = (-36 - 20)\cdot \frac{37}{38})^{36} + \sum_{i=1}^{36}{(36(i-1) + 20) \cdot \binom{36}{i} (\frac{37}{38})^{36-i}(\frac{1}{38})^i} ≈ 2.7904190810856586
        $$


??? tip "概率&期望的具体计算 (Calculation of probability & expectation)"

    ```python exec="true" source="material-block" session="fifty-7"
    --8<-- "docs/fifty/snippet/7_curing_compulsive_gambler.py:solution1"
    ```





### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        The overall process of the game is relatively simple, and we can simulate it through the following code:

        ```python exec="true" source="material-block" session="fifty-7"
        --8<-- "docs/fifty/snippet/7_curing_compulsive_gambler.py:solution2"
        ```


    === "中文"

        游戏的过程总体比较简单，我们可以通过下面的代码来模拟:

        ```python exec="true" source="material-block" session="fifty-7"
        --8<-- "docs/fifty/snippet/7_curing_compulsive_gambler.py:solution2"
        ```
