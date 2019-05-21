# 题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

### solution 1：暴力解
两重循环，第一层遍历x，第一层循环其余元素y。如果x+y=target：成功。
暴力、简单、耗时。

### solution 2：
一层遍历x，查看target-x是否在nums中。
注意：由于不能重复利用同样的元素，因此遍历一个x，要将x去掉(pop)。

### solution 3：Map（最优）
一次遍历x，建立一个HashMap(dict)，将{key: value}:{target-x: index}存入字典中。
如果target-x在字典中，那么target-x的value即为对应元素的index。
