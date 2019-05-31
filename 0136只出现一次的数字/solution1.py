class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while nums:
            x = nums.pop(0)
            if x in nums:
                nums.remove(x)
            else:
                return x


if __name__ == "__main__":
    x = [4, 1, 2, 1, 2]
    print(Solution().singleNumber(x))
