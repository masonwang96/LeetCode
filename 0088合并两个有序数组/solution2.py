class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1 = nums1[:m]
        nums1.extend(nums2)
        nums1.sort()
        print(nums1)


if __name__ == "__main__":
    x = [1, 2, 3, 0, 0, 0]
    y = [2, 5, 6]
    Solution().merge(x, 3, y, 3)
