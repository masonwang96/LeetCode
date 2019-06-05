class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = []
        for i in list(set(nums)):
            if nums.count(i) > len(nums) / 2:
                return i


if __name__ == "__main__":
    x = [3, 2, 3]
    print(Solution().majorityElement(x))
