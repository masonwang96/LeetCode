class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                j += 1
            else:
                i += 1
        nums.extend([0] * j)

        print(nums)


if __name__ == "__main__":
    x = [0, 1, 0, 3, 12]
    print(Solution().moveZeroes(x))
