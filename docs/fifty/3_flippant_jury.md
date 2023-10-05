# The Flippant Juror

## Problem

???+ question "Question"

    === "English"

        A three-man jury has two members each of whom independently 
        has probability $p$ of making the correct decision 
        and a third member who flips a coin for each decision (majority rules).
        A one-man jury has probability $p$ of making the correct decision. 
        Which jury has the better probability of making the correct decision?


    === "中文"

        三人陪审团有两名成员，每人独立地有 $p$ 做出正确决定的概率，
        第三名成员则为每个决定掷硬币（多数规则）。 一人陪审团做出正确决定的概率为 $p$。 
        哪个陪审团做出正确决定的可能性更大？


## Tip

??? tip "Tip"

    === "English"

        Total probability formula

    === "中文"

        全概率公式


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"
    
        Firstly, the probability of an individual juror making the correct judgment is straightforward and is denoted as $p$.
        
        In the case of a three-person jury, the probability can be divided into two parts based on whether the third member is randomly selected correctly. If the result of the random selection by the third member is the correct answer, according to the majority voting rule, it is sufficient for one of the first two members to make the correct judgment. In this case, the probability is:
        
        $$\frac{1}{2}[1 - (1 - p)^2]$$
    
        If the result of the random selection by the third member is the correct answer, according to the majority voting rule, both of the first two members must make the correct judgment. In this case, the probability is: 
    
        $$\frac{1}{2} \times p \times p = \frac{1}{2}p^2$$
        
        Therefore, the probability of obtaining the correct judgment in a three-person jury is:
    
        $$\frac{1}{2}[1 - (1 - p)^2] + \frac{1}{2}p^2 = p$$
    
        Thus, the likelihood of both juries making the correct decision is the same and equal to $p$.


    === "中文"

        首先一人陪审团做出正确判决的概率很简单，就是$p$。
        
        三人陪审团时，概率可以按照第三名成员是否随机选中了正确的判决分成两部分。
        如果第三名成员随机选择的结果是正确答案，那么根据多数投票规则，
        只要前两名成员中有一人做出正确的判决即可，此时概率为：
        
        $$\frac{1}{2}[1 - (1 - p)^2]$$

        如果第三名成员随机选择的结果是正确答案，那么根据多数投票规则，
        只要前两名成员必须都做出正确的判决才可以，此时概率为： 

        $$\frac{1}{2} \times p \times p = \frac{1}{2}p^2$$
        
        由此得到三人陪审团时得到正确判决的概率是：

        $$\frac{1}{2}[1 - (1 - p)^2] + \frac{1}{2}p^2 = p$$

        所以两个陪审团做出正确决定的可能性一样大，都是$p$



### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        The probability of obtaining the correct verdict at this time 
        can be approximated by simulating the judgment process of a three-person jury.

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/3_flippant_jury.py:solution2"
        ```


    === "中文"

        可以通过模拟三人陪审团的判决过程来近似得到此时得到正确判决的概率。

        ```python exec="true" source="material-block" session="fifty-2"
        --8<-- "docs/fifty/snippet/3_flippant_jury.py:solution2"
        ```
