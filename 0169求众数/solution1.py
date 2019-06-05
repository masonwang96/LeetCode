class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        return max(d, key=d.get)


if __name__ == "__main__":
    x = [3, 2, 3]
    print(Solution().majorityElement(x))
