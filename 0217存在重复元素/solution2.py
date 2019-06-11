class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        while nums:
            if not nums[0] in d:
                d[nums[0]] = 1
                nums.pop(0)
            else:
                return True

        return False


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().containsDuplicate(x))
