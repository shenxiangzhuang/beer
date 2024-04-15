---
title: About Beer
draft: false
date: 2024-04-15
authors: [mathew]
slug: about-beer
description: >
    Beer: Challenging Problems in Probability and Statistics
categories:
  - General

toc_depth: 3
---

## Why :beer:

相信很多统计学相关专业的同学都知道Box-Cox变换，这里Box就是统计学巨擘George E. P. Box.
在其讣告[Renowned statistician George Box dies at 93](https://news.wisc.edu/renowned-statistician-george-box-dies-at-93/)
中有这么一段关于Monday night beer and statistics sessions介绍(这在其传记中也有相关的介绍)。

!!! quote "Monday night beer and statistics sessions"

    Best known on campus were the **Monday night beer and statistics sessions** Box hosted at his home for students
    and other researchers. The gatherings sparked lively discussions about how statistics could help solve research
    problems posed by speakers from a wide range of disciplines.

<!-- more -->

这种积极开放，共同探讨统计学如何用于解决问题的方式着实令人神往。
即使是在读书的时候我也很少有机会和大家像这样一起讨论有趣的问题。

后来读研有时会和室友@SY一起解一些概率统计/算法题目，有些是游戏相关面试题(1)，有些是自己遇到的一些中大复试考研题(2) ,
有些来自Tomorrow学长的[博客](https://yuanhang0.github.io/), 这期间我也自己写过一些相关的文章(3)。
{ .annotate }

1. :fontawesome-regular-face-laugh-wink: [游戏中的概率问题——有趣的概率问题（一）](https://mp.weixin.qq.com/s/mCZB1NMsdvg7og6IVWVs2g):
之前和@SY讨论过的一些问题感觉很有意思，就拜托他找时间整理了下来。
2. :fontawesome-regular-face-laugh-wink: [A Fair Game Problem](https://yuanhang0.github.io/posts/A-Fair-Game-Problem):
中大考研复试的一道题，@SY给我讲了两遍没听懂，又找Tomorrow学长帮忙写的一个解析:)
3. [Three doors and three prisoners](https://datahonor.com/datascience/statistics/three-doors-and-three-prisoners/)


这些问题的本身就趣味十足，解决的方法更是灵活多变: 可以用朴素的概率统计思想求解，也可以用很“取巧”(1)的方式来快速得到答案，
也可以写代码来模拟问题得到数值解。对我来说，当一个有趣的问题通过多种截然不同的方式得到相同的结果时，那种喜悦是难以言表的。
{ .annotate }

1. 只是看似取巧而已，其能快速解决问题还是因为这种解法更加接近于问题的本质。

这是读书时的一些经历，算是Beer项目的萌芽阶段。

## Past/Now/Future

### Past

后来工作，从另外的角度的见识到了概率统计的作用，基于概率统计的方法一般简洁优雅，复杂度低且具有很强的可解释性——这些
特质使得其成为算法落地时很好的选择。

这种在真实世界发挥作用的方式让我对概率统计的认识得到了很大的拓展。读书时候学到的那些抽象的概念: 帕累托分布，游程检验，
Wilcoxon-Mann-Whitney statistic等等这些都变得鲜活起来——这同样让我感觉非常地快乐。

我和同事提过说有机会的话我也想试试搞下类似Monday night beer and statistics sessions的东西，
他说很感兴趣，让我到时候喊他一起——可惜由于种种原因，此事一直未能成行:)

### Now

后来偶然看到*Fifty challenging problems in probability*这本书，发现了书中记录了很多有趣的问题。
这一次我决定真正开始品尝这杯:beer，于是就有了现在的[Beer](https://datahonor.com/beer), 目前主要是
*Fifty challenging problems in probability*书中几个问题的解答: [Beer/Fifty](https://datahonor.com/beer/fifty/).

目前对于每个问题都提供了详细的描述，提示，解析解，数值模拟代码，下面是第一道题的题干和对应的答案。
这里重点提下，**模拟程序的代码是运行在浏览器的**，也就是说每次我们刷新网页，这个模拟就会执行一次全新的模拟。

[//]: # (???+ note "Question & Solution")

{% include-markdown "fifty/1_the_sock_drawer.md" heading-offset=3 %}


### Future
关于:beer:的未来，现在的计划主要是分成三部分: 类似Fifty这种习题集单独一个部分，各类记录在各个地方的无出处可考的题目作为一个部分，
最后一部分是工业界一些的实际的案例。
目前是专注在第一部分，后续的Roadmap会更新到[Issue](https://github.com/shenxiangzhuang/beer/issues)。


## Help Wanted
个人的力量终究是有限的，欢迎大家一起参与建设，一起感受概率统计的乐趣。
欢迎各类贡献: 提建议，提供题目，提供解答等都可以。

其实只要了解概率统计基础知识和基本的编程知识就可以试着做一些代码贡献了，
如果大家在PR过程中遇到问题欢迎在[Discussion](https://github.com/shenxiangzhuang/beer/discussions)提问，
我会尽量帮助大家解决！
