class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        while 0 in nums:
            nums.remove(0)
            i += 1
        nums.extend([0] * i)

        print(nums)


if __name__ == "__main__":
    x = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(x))
