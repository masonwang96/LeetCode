class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        length = len(nums)
        while i != length:
            if nums[i] == val:
                nums.pop(i)
                length -= 1
            else:
                i += 1
        return i


if __name__ == "__main__":
    x = [3, 2, 2, 3]
    y = 3
    print(Solution().removeElement(x, y))
    assert (Solution().removeElement(x, y) == 2)
    x = [0, 1, 2, 2, 3, 0, 4, 2]
    y = 2
    print(Solution().removeElement(x, y))
    assert (Solution().removeElement(x, y) == 5)
