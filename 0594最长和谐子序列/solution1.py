class Solution:
    def findLHS(self, nums: [int]) -> int:
        res = 0
        for num in nums:
            temp = [x for x in nums if x == num - 1 or x == num]
            if len(set(temp)) == 1:
                continue
            res = max(res, len(temp))
        return res


if __name__ == "__main__":
    x = [1, 3, 2, 2, 5, 2, 3, 7]
    x = [1, 1, 1, 1]
    print(Solution().findLHS(x))
