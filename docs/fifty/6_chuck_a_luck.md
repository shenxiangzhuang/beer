# Chuck-a-Luck

## Problem

???+ question "Question"

    === "English"

        Chuck-a-Luck is a gambling game often played at carnivals and gambling houses. 
        A player may bet on anyone of the numbers 1,2,3,4,5,6. 
        Three dice are rolled. If the player's number appears on one, two, or three of the dice, 
        he receives respectively one, two, or three times his original stake plus his own money back; 
        otherwise he loses his stake. What is the player's expected loss per unit stake? 
        (Actually the player may distribute stakes on several numbers, 
        but each such stake can be regarded as a separate bet.)

    === "中文"

        Chuck-a-Luck是一种常在嘉年华和赌场中玩的赌博游戏。
        玩家可以押注1、2、3、4、5或6中的任意一个数字。三个骰子被投掷，如果玩家押注的数字出现在一个、两个或三个骰子中，
        他将分别获得其原始赌注的一倍、两倍或三倍以及自己的本金；否则他将输掉他的赌注。
        玩家每投注一单位，他的预期损失是多少？（实际上，玩家可以在几个数字上分配赌注，但每个赌注可以视为一次单独的押注。）


## Tip

??? tip "Tip"

    === "English"

        Since we are looking for expectations, we need to first define the random variable, 
        then find out the probability of its distribution, and finally find the expectations.

    === "中文"

        既然是求期望，那么我们需要先定义随机变量，然后找出其分布的概率，最后求期望即可。


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        Let $R$ be the player's reward and $S$ be the original stake. Then the player's expected reward is $E(R)$, and the expected loss is $E(L) = -E(R)$.
    
        To find $E(R)$, we first list the distribution of $R$ as follows:
        
        |   | $R$   | Probability | Calculation Result |
        |---|-------|-------------|--------------------|
        | 1 | $-S$  | $\left[\frac{5}{6}\right]^3$ | $\frac{125}{216}$ |
        | 2 | $S$   | $\frac{1}{6}\cdot\frac{5}{6}\cdot\frac{5}{6} + \frac{5}{6}\cdot\frac{1}{6}\cdot\frac{5}{6} + \frac{5}{6}\cdot\frac{5}{6}\cdot\frac{1}{6}$ | $\frac{75}{216}$ |
        | 3 | $2S$  | $\frac{1}{6}\cdot\frac{1}{6}\cdot\frac{5}{6} + \frac{1}{6}\cdot\frac{5}{6}\cdot\frac{1}{6} + \frac{5}{6}\cdot\frac{1}{6}\cdot\frac{1}{6}$ | $\frac{15}{216}$ |
        | 4 | $3S$  | $\left[\frac{1}{6}\right]^3$ | $\frac{1}{216}$ |
        
        From this, we can compute:
        
        $$
        E(R) = -S\cdot\frac{125}{216} + S\cdot\frac{75}{216} + 2S\cdot\frac{15}{216} + 3S\cdot\frac{1}{216} = -\frac{17}{216}S
        $$
        
        $$ 
        E(L) = -E(R) = \frac{17}{216}S
        $$

    === "中文"

        记玩家的奖励为$R$，原始的赌注为$S$，那么玩家的预期奖励为$E(R)$,
        预期的损失为$E(L) = -E(R)$.
        因为要求$E(R)$，所以我们先列出$R$的分布，如下：
        
        |   | $R$   | Probability | Calculation Result |
        |---|-------|-------------|--------------------|
        | 1 | $-S$  | $\left[\frac{5}{6}\right]^3$ | $\frac{125}{216}$ |
        | 2 | $S$   | $\frac{1}{6}\cdot\frac{5}{6}\cdot\frac{5}{6} + \frac{5}{6}\cdot\frac{1}{6}\cdot\frac{5}{6} + \frac{5}{6}\cdot\frac{5}{6}\cdot\frac{1}{6}$ | $\frac{75}{216}$ |
        | 3 | $2S$  | $\frac{1}{6}\cdot\frac{1}{6}\cdot\frac{5}{6} + \frac{1}{6}\cdot\frac{5}{6}\cdot\frac{1}{6} + \frac{5}{6}\cdot\frac{1}{6}\cdot\frac{1}{6}$ | $\frac{15}{216}$ |
        | 4 | $3S$  | $\left[\frac{1}{6}\right]^3$ | $\frac{1}{216}$ |
        
        由此计算出
        
        $$
            E(R) = -S\cdot\frac{125}{216} + S\cdot\frac{75}{216} + 2S\cdot\frac{15}{216} + 3S\cdot\frac{1}{216} = -\frac{17}{216}S
        $$

        $$ 
            E(L) = -E(R) = \frac{17}{216}S
        $$

### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        We can also simulate the game to find the expected loss:
        ```python exec="true" source="material-block" session="fifty-6"
        --8<-- "docs/fifty/snippet/6_chuck_a_luck.py:solution2"
        ```

    === "中文"
        
        可以直接模拟整个赌博过程来获取近似的结果:
        
        ```python exec="true" source="material-block" session="fifty-6"
        --8<-- "docs/fifty/snippet/6_chuck_a_luck.py:solution2"
        ```
