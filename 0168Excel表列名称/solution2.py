class Solution(object):
    def singleNumber(self, nums):
        """
        可用异或运算快速找到只出现一次的数字
        两个相同的数字做异或运算结果为0；0与非0数字做异或运算结果为非零运算
         :type nums: List[int]
        :rtype: int
       """
        singel_num = 0
        for num in nums:
            singel_num ^= num
        return singel_num


if __name__ == "__main__":
    x = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(x))
