class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        s = sum(nums[0:k])
        res = s
        for i in range(1, len(nums) - k + 1):
            s = s - nums[i - 1] + nums[i + k - 1]
            res = max(res, s)
        return res / k


if __name__ == "__main__":
    x = [1, 12, -5, -6, 50, 3]
    y = 4
    x = [0, 1, 1, 3, 3]
    y = 4
    print(Solution().findMaxAverage(x, y))
