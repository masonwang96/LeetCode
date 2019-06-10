class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = []
        while nums1 and nums2:
            if nums1[0] in nums2:
                inter.append(nums1[0])
                nums2.remove(nums1[0])
                nums1.pop(0)
            else:
                nums1.pop(0)
        return inter


if __name__ == "__main__":
    x = [1, 2, 2, 1]
    y = [2, 2]
    print(Solution().intersection(x, y))
