# Perfect Bridge Hand

## Problem

???+ question "Question"

    === "English"

        We often read of someone who has been dealt 13 spades at bridge. With
        a well-shuffled pack of cards, what is the chance that you are dealt a perfect
        hand (13 of one suit)? (Bridge is played with an ordinary pack of 52 cards,
        13 in each of 4 suits, and each of 4 players is dealt 13.)

    === "中文"

        桥牌是用一叠普通的 52 张牌打的，4 种花色各 13 张，4 名玩家每人发 13 张。
        我们经常读到有人在桥牌上拿到了 13 张黑桃。 一副洗好后的牌，你拿到完美牌（同花色 13 张）的机会有多大？
        


## Tip

??? tip "Tip"

    === "English"

        Enumeration: situations where a flush is drawn/all situations where a random card is drawn

    === "中文"

        枚举: 抓到同花的情况/所有随机抓牌情况


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        All possible card drawing situations, where each person randomly draws 13 cards
        (in a completely random situation, drawing 13 cards at once and drawing one card per round for 13 rounds are equivalent):

        $$
            \binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}
        $$
        
        We draw the same suit, and since there is no restriction on the suit,
        it can be any one of the 4 suits:

        $$
        4 \cdot \binom{13}{13}
        $$

        Therefore, we can calculate the probability of drawing the same suit as:

        $$
        \begin{align}
        p &= \frac{4 \cdot \binom{13}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}}{\binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}} \\
          &= \frac{4 \cdot \binom{13}{13}}{\binom{52}{13}} = \frac{4}{\binom{52}{13}} = \frac{4}{\frac{52!}{13!39!}} \\
          &= 4 \cdot \frac{13!39!}{52!} = \frac{12!39!}{51!}
        \end{align}
        $$

        We can use Python to calculate the corresponding probability as:

        ```python exec="true" source="material-block" session="fifty-8"
        --8<-- "docs/fifty/snippet/8_perfect_bridge_hand.py:solution1"
        ```

    === "中文"

        所有抓牌的情况, 每人随机抓13张牌(在牌完全随机的情况下，每人一次抓13张牌和每轮一张，抓13轮是一致的):

        $$
            \binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}
        $$
        
        我们抓出同花的情况，因为没有限制花色，所以可以是4个花色中的任意一个:

        $$
        4 \cdot \binom{13}{13}
        $$

        由此计算出我们抓到同花的概率为

        $$
        \begin{align}
        p &= \frac{4 \cdot \binom{13}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}}{\binom{52}{13}\binom{39}{13}\binom{26}{13}\binom{13}{13}} \\
          &= \frac{4 \cdot \binom{13}{13}}{\binom{52}{13}} = \frac{4}{\binom{52}{13}} = \frac{4}{\frac{52!}{13!39!}} \\
          &= 4 \cdot \frac{13!39!}{52!} = \frac{12!39!}{51!}
        \end{align}
        $$

        我们可以用Python计算出对应的概率为:

        ```python exec="true" source="material-block" session="fifty-8"
        --8<-- "docs/fifty/snippet/8_perfect_bridge_hand.py:solution1"
        ```



### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"
        We can directly simulate the card drawing process to get exactly the same result.
        Here we simulate the situation of drawing one card in each round: a total of 4 cards are drawn in each round, 
        one of which is of the same suit.
        During simulation, we calculate the probability of each round and multiply the probabilities of each round 
        to get the final probability.

        The simulation results are as follows:

        ```python exec="true" source="material-block" session="fifty-8"
        --8<-- "docs/fifty/snippet/8_perfect_bridge_hand.py:solution2"
        ```

    === "中文"

        我们可以直接模拟抓牌过程来得到完全一致的结果，这里模拟每轮抓一张牌的情况: 每轮共抽取4张牌，其中一张牌为同一个花色。
        模拟时，我们计算每轮的概率，将每轮的概率乘起来得到最终的概率。

        模拟结果如下:

        ```python exec="true" source="material-block" session="fifty-8"
        --8<-- "docs/fifty/snippet/8_perfect_bridge_hand.py:solution2"
        ```
