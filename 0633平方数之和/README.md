# 题目描述
给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:

    输入: 5
    输出: True
    解释: 1 * 1 + 2 * 2 = 5
     

示例2:

    输入: 3
    输出: False

### solution 1：
从0开始，依次判断c-i**2是否是平方数。

### solution 2：
双指针

i 从 0 开始
j 从可取的最大数 int(math.sqrt(c)) 开始

    total = i * i + j * j
    total > c: j = j - 1，将 total 值减小
    total < c: i = i + 1，将 total 值增大
    total == c：返回 True