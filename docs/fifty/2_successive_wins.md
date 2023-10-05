# Successive Wins

## Problem

???+ question "Question"

    === "English"

        To encourage Elmer's promising tennis career,
        his father offers him a prize if he wins (at least) two tennis sets
        in a row in a three-set series to be played with his father
        and the club champion alternately:
        father-champion- father or champion-father-champion,
        according to Elmer's choice. The champion is a better player than
        Elmer's father. Which series should Elmer choose?

    === "中文"

        为了鼓励Elmer有前途的网球生涯，如果他在三盘系列赛中连续赢得（至少）两盘网球，
        他的父亲就会向他提供奖励。比赛形式是与他的父亲和俱乐部冠军进行交替比赛，
        Elmer可以选择以下两种比赛顺序中的一种：<父亲-冠军-父亲>或<冠军-父亲-冠军>。
        冠军是比Elmer的父亲更好的球员。Elmer应该选择哪个比赛顺序？


## Tip

??? tip "Tip"

    === "English"

        Pay attention to the conditions for winning two games in a row **consecutively**

    === "中文"

        注意这里**连续**赢两场的条件


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        Let's denote the father as F, the champion as C,
        and the probabilities of Elmer winning against the father
        and the champion as $f$ and $c$, respectively.
        Since the champion is stronger, we have $f > c$.
        If we consider the sequence FCF,
        Elmer can win the reward in the following three cases:

        <div align="center">

        | F | C | F | Probability|
        |---|---|---|---|
        | ✅ | ✅ | ✅ | $fcf$ |
        | ✅ | ✅ | ❌ | $fc(1-f)$ |
        | ❌ | ✅ | ✅ | $(1-f)cf$ |

        </div>

        The probability of Elmer winning the reward in this case is:

        $$fcf + fc(1-f) + (1-f)cf = fc(2-f)$$

        Similarly, if we consider the sequence CFC,
        Elmer can win the reward in the following three cases:

        <div align="center">

        | C | F | C | Probability|
        |---|---|---|---|
        | ✅ | ✅ | ✅ | $cfc$ |
        | ✅ | ✅ | ❌ | $cf(1-c)$ |
        | ❌ | ✅ | ✅ | $(1-c)fc$ |

        </div>

        The probability of Elmer winning the reward in this case is:

        $$cfc + cf(1-c) + (1-c)fc = fc(2-c)$$

        Since

        $$f > c$$

        we have

        $$P(FCF) = fc(2-f) < fc(2-c) = P(CFC)$$

        Therefore, Elmer has a higher probability of winning
        the reward if he chooses the sequence CFC.


    === "中文"

        这里记父亲为F，冠军为C，Elmer和父亲和冠军比赛获胜的概率分别是
        $f$, $c$。因为冠军实力更强，所以有$f > c$。
        如果选择FCF的顺序，那么Elmer赢得奖励的情况有如下三种:

        <div align="center">

        | F | C | F | Probability|
        |---|---|---|---|
        | ✅ | ✅ | ✅ | $fcf$ |
        | ✅ | ✅ | ❌ | $fc(1-f)$ |
        | ❌ | ✅ | ✅ | $(1-f)cf$ |

        </div>

        得到此时Elmer赢得奖励的概率为:

        $$fcf + fc(1-f) + (1-f)cf = fc(2-f)$$

        同理，如果选择CFC的顺序，那么Elmer赢得奖励的情况有如下三种:

        <div align="center">

        | C | F | C | Probability|
        |---|---|---|---|
        | ✅ | ✅ | ✅ | $cfc$ |
        | ✅ | ✅ | ❌ | $cf(1-c)$ |
        | ❌ | ✅ | ✅ | $(1-c)fc$ |

        </div>

        得到此时Elmer赢得奖励的概率为:

        $$ cfc + cf(1-c) + (1-c)fc = fc(2-c) $$

        因为

        $$f > c$$

        所以

        $$P(FCF) = fc(2-f) < fc(2-c) = P(CFC)$$

        即Elmer选择CFC的顺序比赛赢得奖励的概率更高


### Solution2: Simulation


??? success "Solution2: Simulation"

    === "English"

        We can simulate the CFC and FCF sequences using the following approach:

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/2_successive_wins.py:solution2"
        ```

        Since the probabilities `f` and `c` for winning against the father and the champion are randomly generated using `get_prior_prob`, the results may vary for each simulation. However, we can observe that the probability for the CFC sequence is slightly higher.


        If we carefully analyze this simulation experiment, we can identify a limitation: it only simulates one pair of `f` and `c` probabilities. Therefore, the higher probability for CFC compared to FCF might be due to chance. To validate if CFC consistently has a higher probability than FCF, we need to simulate different configurations of `f` and `c`.

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/2_successive_wins.py:solution2-extend"
        ```

        Hence, we have sufficient data to conclude that the probability of CFC being greater than FCF is consistent.


    === "中文"

        可以通过下面的方式进行CFC，FCF两个模式的比赛模拟:

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/2_successive_wins.py:solution2"
        ```

        因为这里赢得父亲和冠军的概率`f`, `c`是通过`get_prior_prob`随机生成，
        所以每次模拟的结果会不相同。但是都能够看到CFC顺序的概率更高一些.

        如果我们仔细思考这个模拟实验就会发现其中还有不足的地方，那就是这里只模拟了一对
        `f`, `c`概率下的情况。那么这里模拟得到的CFC的概率大于FCF的概率不排除是偶然的原因。
        所以我们需要模拟在不同`f`, `c`配置下是否都有CFC的概率大于FCF的概率。

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/2_successive_wins.py:solution2-extend"
        ```

        至此，我们有充足的数据说明CFC的概率大于FCF的概率。
