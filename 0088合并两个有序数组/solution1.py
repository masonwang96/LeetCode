class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return nums1
        nums1 = nums1[:m]
        i = 0
        while i < m and nums2:
            if nums1[i] >= nums2[0]:
                nums1.insert(i, nums2.pop(0))
                i += 2
            else:
                i += 1
        nums1.extend(nums2)
        print(nums1)


if __name__ == "__main__":
    x = [1, 2, 3, 0, 0, 0]
    y = [2, 5, 6]
    Solution().merge(x, 3, y, 3)
