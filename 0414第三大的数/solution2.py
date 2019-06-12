class Solution:
    def thirdMax(self, nums: [int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        for i in range(2):
            times = nums.count(max(nums))
            for j in range(times):
                nums.remove(max(nums))
        return max(nums)


if __name__ == "__main__":
    x = [3, 2, 1]
    x = [2, 2, 3, 1]
    x = [1, -2147483648, 2]
    # x = [5, 2, 4, 1, 3, 6, 0]
    print(Solution().thirdMax(x))
