class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        while nums:
            temp = nums[0]
            nums.pop(0)
            if temp in nums:
                return True

        return False


if __name__ == "__main__":
    x = [1, 1, 2, 3, 4, 5, 6, 7]
    print(Solution().containsDuplicate(x))
