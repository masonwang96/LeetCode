# 题目描述
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

    输入: numbers = [2, 7, 11, 15], target = 9
    输出: [1,2]
    解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
    
### solution 1：HashMap
一次遍历x，建立一个HashMap(dict)，将{key: value}:{target-x: index}存入字典中。
如果target-x在字典中，那么target-x的value即为对应元素的index。

### solution 2：双指针
使用两个指针i和j，分别指向numbers首尾：当i<j时，如果xi+xj>target,
那么只能将j左移；如果xi+xj<target，那么只能将i右移。

相当于遍历n/2长度。

### solution 3：HashMap
solution 1的另外一种实现。

### solution 4：HashMap
solution 1的另外一种实现。

