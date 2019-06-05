class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, res = 0, -1
        for num in nums:
            if count == 0:
                res = num
            if num == res:
                count += 1
            else:
                count -= 1

        return res


if __name__ == "__main__":
    x = [3, 2, 2]
    print(Solution().majorityElement(x))
