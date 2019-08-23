class Solution:
    def findShortestSubArray(self, nums: [int]) -> int:
        # 用字典保存元素及其对应的出现位置
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        # 找到出现最多的次数（数组的度）
        freq = 0
        for i in d:
            freq = max(freq, len(d[i]))
        # 找到出现次数对于度的元素的子数组长度
        res = len(nums)
        for i in d:
            if len(d[i]) == freq:
                res = min(res, d[i][-1] - d[i][0] + 1)

        return res


if __name__ == "__main__":
    x = [1, 2, 2, 3, 1]
    print(Solution().findShortestSubArray(x))
