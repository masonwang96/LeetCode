# 题目描述
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串

示例 1：
    
    输入: "Hello"
    输出: "hello"
示例 2：
    
    输入: "here"
    输出: "here"
示例 3：
    
    输入: "LOVELY"
    输出: "lovely"

### solution 1：
直接使用str.lower()....

### solution 2：
遍历字符串，每个大写字符ASCII码加32.

### solution 3：
先建立dict映射大写字母到小写字母，再遍历字符串，根据情况转化为小写。

