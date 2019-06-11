class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def swap1(nums):
            i = len(nums) - 1
            while i > 0:
                temp = nums[i]
                nums[i] = nums[i - 1]
                nums[i - 1] = temp
                i -= 1

        k = k % len(nums)
        while k > 0:
            swap1(nums)
            k -= 1



if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().rotate(x, k))
