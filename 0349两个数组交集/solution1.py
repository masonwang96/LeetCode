class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set([x for x in nums1 if x in nums2])


if __name__ == "__main__":
    x = [1, 2, 2, 1]
    y = [2, 2]
    print(Solution().intersection(x, y))
