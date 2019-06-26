class Solution:
    def findLHS(self, nums: [int]) -> int:
        d = {}
        res = 0
        # for x in nums:
        #     if x not in d.keys():
        #         d[x] = nums.count(x)
        """上面这种建立字典较耗时，要用下面这种"""
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for key in d.keys():
            if key - 1 in d.keys():
                res = max(res, d.get(key) + d.get(key - 1, 0))
        return res


if __name__ == "__main__":
    x = [1, 3, 2, 2, 5, 2, 3, 7]
    x = [1, 1, 1, 1]
    print(Solution().findLHS(x))
