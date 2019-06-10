class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:] = list(reversed(nums[:k])) + list(reversed(nums[k:]))


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(Solution().rotate(x, k))
