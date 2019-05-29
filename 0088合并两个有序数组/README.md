# 题目描述
给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
示例:

    输入:
    nums1 = [1,2,3,0,0,0], m = 3
    nums2 = [2,5,6],       n = 3
    
    输出: [1,2,2,3,5,6]
    
### solution 1：
遍历一次，不断比较nums1和nums2的元素。若nums1[i]大于等于
nums2的第一个元素，则将nums2的第一个元素pop，并
插入nums1[i]前面。
### solution 2：
耍赖级。直接将nums2插入nums1，并用.sort排序。