class Solution:
    def findMaxAverage(self, nums: [int], k: int) -> float:
        res = []
        for i in range(len(nums) - k+1):
            res.append(sum(nums[i:i + k]))
        return max(res) / k


if __name__ == "__main__":
    x = [1, 12, -5, -6, 50, 3]
    y = 4
    print(Solution().findMaxAverage(x, y))
