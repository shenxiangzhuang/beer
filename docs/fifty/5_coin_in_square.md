# Coin in Square

## Problem

???+ question "Question"

    === "English"

        In a common carnival game a player tosses a penny from a distance of
        about 5 feet onto the surface of a table ruled in 1-inch squares.
        If the penny ($\frac{3}{4}$ inch in diameter) falls entirely
        inside a square, the player receives 5 cents but does not
        get his penny back; otherwise he loses his penny.
        If the penny lands on the table, what is his chance to win?

    === "中文"

        在一个常见的嘉年华游戏中，玩家从大约5英尺的距离上将一枚一美分硬币投掷到一个划分为1英寸方格的桌面上。
        如果硬币（直径为$\frac{3}{4}$英寸）完全落在一个方格内，玩家将获得5美分，
        但不会拿回他的硬币；否则，他将失去他的硬币。如果硬币落在桌子上，他获胜的机会有多大？


## Tip

??? tip "Tip"

    === "English"

        Consider the point where the center of the coin’s circle falls

    === "中文"

        考虑硬币圆心的落点


## Solutions

### Solution1: Analysis

??? success "Solution1: Analysis"

    === "English"

        The key to solving this problem lies in recognizing that
        the crucial factor is the position of the coin's center within the square.

        Since the square has a length and width of 1 inch,
        and the coin has a diameter of $\frac{3}{4}$ inch,
        when the center of the coin is at the center of the square,
        the coin completely falls within the square.
        Additionally, there are some gaps between the coin and the edges
        of the square in all directions.

        To determine the winning probability,
        we consider the region where the center of the coin moves up, down, left, and right
        from the center until it touches one of the boundaries of the square.
        The area covered by the center during this movement represents all the valid positions for the center.

        The calculation of this area is straightforward.
        Based on the symmetry between the circle and the square,
        the region is determined by four points adjacent to the square's vertices.
        Each of these points is at a vertical distance of the coin's radius, which is $\frac{3}{8}$ inch.
        Therefore, the area of the region within these four points, which corresponds to the winning region, is:

        $$(1 - \frac{3}{8} - \frac{3}{8})^2 = (\frac{1}{4})^2 = \frac{1}{16}$$


    === "中文"

        这里解题的关键在于识别到核心在于硬币圆心在方格内的落点。

        因为方格长宽均为1英寸，硬币直径为$\frac{3}{4}$英寸，
        所以当硬币圆心在方格中心时，硬币就是整个都落入方格。
        此外硬币和方格的上下左右之间都还有一些缝隙，
        此时将硬币以此为中心向上下左右活动，直到某一个边界和方格相切，这期间
        圆心滑过的区域就是所有符合条件的圆心的位置。
        这个区域的面积除以方格的面积就是获胜的概率。

        具体定位这个圆心区域的方式也很简单，根据圆和正方形的对称性，这里的区域由
        临近方格顶点的四个点决定，每个点离最近方格边的垂直距离均为硬币的半径，
        即$\frac{3}{8}$英尺。所以得到四个点内区域即获胜区域的面积为

        $$(1 - \frac{3}{8} - \frac{3}{8})^ 2 = (\frac{1}{4})^2 = \frac{1}{16}$$



### Solution2: Simulation

??? success "Solution2: Simulation"

    === "English"

        The probability of winning can be approximated by simulating the throwing process

        ```python exec="true" source="material-block" session="fifty-5"
        --8<-- "docs/fifty/snippet/5_coin_in_square.py:solution2"
        ```

        We can also visualize simulation experiments to get an intuitive feeling

        ```python exec="true" html="1" source="tabbed-right" title="simulation plot" session="fifty-5"
        --8<-- "docs/fifty/snippet/5_coin_in_square.py:solution2-plot"
        ```

    === "中文"

        可以通过模拟投掷的过程来近似求解获胜的概率

        ```python exec="true" source="material-block" session="fifty-5"
        --8<-- "docs/fifty/snippet/5_coin_in_square.py:solution2"
        ```

        我们也可以将模拟实验可视化来获取直观的感受
        ```python exec="true" html="1" source="tabbed-right" title="simulation plot" session="fifty-5"
        --8<-- "docs/fifty/snippet/5_coin_in_square.py:solution2-plot"
        ```
