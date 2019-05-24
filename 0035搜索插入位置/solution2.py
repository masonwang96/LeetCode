class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)


if __name__ == "__main__":
    x = [1, 3, 5, 6]
    y = 5
    print(Solution().searchInsert(x, y))
    assert (Solution().searchInsert(x, y) == 2)
    x = [1, 3, 5, 6]
    y = 2
    print(Solution().searchInsert(x, y))
    assert (Solution().searchInsert(x, y) == 1)
