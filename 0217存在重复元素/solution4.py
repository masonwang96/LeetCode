class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        return True if not len(nums) == len(set(nums)) else False


if __name__ == "__main__":
    x = [1, 1, 2, 3, 4, 5, 6, 7]
    print(Solution().containsDuplicate(x))
