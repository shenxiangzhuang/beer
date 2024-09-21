# Perfect Bridge Hand

## Problem

???+ question "Question"

    === "English"

        The game of craps, played with two dice, is one of America's fastest and most popular gambling games.
        Calculating the odds associated with it is an instructive exercise.
        The rules are these. Only totals for the two dice count.
        The player throws the dice and wins at once if the total for the first throw is 7 or 11,
        loses at once if it is 2, 3, or 12. Any other throw is called his "point."
        If the first throw is a point, the player throws the dice repeatedly
        until he either wins by throwing his point again or loses by throwing 7.
        What is the player's chance to win?

    === "中文"

        掷骰子赌博游戏是美国最迅速和最受欢迎的赌博游戏之一，使用两颗骰子进行。计算相关的赔率是一项有益的练习。
        规则如下：只计算两颗骰子的总和。
        玩家掷骰子，如果第一次掷出的总点数为7或11，则立刻获胜；如果是2、3或12，则立刻输掉。其他点数称为玩家的“点数”。
        如果第一次掷出的点数是一个点数，玩家将反复掷骰子，直到再次掷出点数获胜，或通过掷出7输掉。
        玩家获胜的概率是多少？

## Tip

??? tip "Tip"

    === "English"

        TBD

    === "中文"

        TBD


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        TODO

    === "中文"

        首先，我们可以列出所有可能的点数和对应的概率：

        | /   | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        | 概率 | 1/36 | 2/36 | 3/36 | 4/36 | 5/36 | 6/36 | 5/36 | 4/36 | 3/36 | 2/36 | 1/36 |

        我们将第一次掷骰子获胜的情况记为 $W_1$，输掉的情况记为 $L_1$，得到点数的情况记为 $P_1$。

        那么，首次掷骰子获胜的概率为：

        $$
        P(W_1) = P(7, 11) = \frac{6}{36} + \frac{2}{36} = \frac{8}{36} = \frac{2}{9}
        $$

        同理，首次掷骰子输掉的概率为：

        $$
        P(L_1) = P(2, 3, 12) = \frac{1}{36} + \frac{2}{36} + \frac{1}{36} = \frac{4}{36} = \frac{1}{9}
        $$

        如果首次掷骰子得到点数，那么点数的值可能为4、5、6、8、9、10中的任意一个。
        我们以点数为4的情况为例，计算此时玩家输掉的概率：

        $$
        \begin{align}
        P(L_{p4}) &= P(7) + (1 - P(4) - P(7)) \cdot P(7) + (1 - P(4) - P(7))^2 \cdot P(7) + \cdots \\
                  &= P(7) \cdot (1 + (1 - P(4) - P(7)) + (1 - P(4) - P(7))^2 + \cdots) \\
                  &= P(7) \cdot \frac{1}{1 - (1 - P(4) - P(7))} \\
                  &= P(7) \cdot \frac{1}{P(4) + P(7)} \\
                  &= \frac{6}{36} \cdot \frac{1}{\frac{3}{36} + \frac{6}{36}} \\
                  &= \frac{6}{36} \cdot \frac{1}{\frac{9}{36}} \\
                  &= \frac{2}{3}
        \end{align}
        $$

        同理，我们可以计算得到点数为5、6、8、9、10时玩家输掉的概率分别为：

        $$
        P(L_{p5}) = P(L_{p9}) = \frac{3}{5}
        $$

        $$
        P(L_{p6}) = P(L_{p8}) = \frac{6}{11}
        $$

        $$
        P(L_{p10}) = P(L_{p4}) = \frac{2}{3}
        $$

        由此得到首次掷骰子得到点数且玩家赢的概率为：

        $$
        \begin{align}
        P(L_p)  &= P(4) \cdot (1-P(L_{p4})) + P(5) \cdot (1-P(L_{p5})) + P(6) \cdot (1-P(L_{p6})) + P(8) \cdot (1-P(L_{p8})) + P(9) \cdot (1-P(L_{p9})) + P(10) (1-\cdot P(L_{p10})) \\
                &= \frac{3}{36} \cdot (1-\frac{2}{3}) + \frac{4}{36} \cdot (1-\frac{3}{5}) + \frac{5}{36} \cdot (1-\frac{6}{11}) + \frac{5}{36} \cdot (1-\frac{6}{11}) + \frac{4}{36} \cdot (1-\frac{3}{5}) + \frac{3}{36} \cdot (1-\frac{2}{3}) \\
                &= \frac{1}{36} + \frac{2}{45} + \frac{25}{396} + \frac{25}{396} + \frac{2}{45} + \frac{1}{36} \\
                &= \frac{134}{495}
        \end{align}
        $$

        所以得到玩家总的获胜概率为：

        $$
        P(W) = P(W_1) + P(W_p) = \frac{2}{9} + \frac{134}{495} = \frac{244}{495} \approx 0.49293
        $$

        所以玩家获胜的概率为约为49.293%。



### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"
        TODO

    === "中文"

        TODO
