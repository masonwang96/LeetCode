class Solution:
    def findLHS(self, nums: [int]) -> int:
        res = []
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if i + 1 in d:
                res.append(d[i] + d[i + 1])
        if res == []:
            return 0
        return max(res)


if __name__ == "__main__":
    x = [1, 3, 2, 2, 5, 2, 3, 7]
    x = [1, 1, 1, 1]
    print(Solution().findLHS(x))
