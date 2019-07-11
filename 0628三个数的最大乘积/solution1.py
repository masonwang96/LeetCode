class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        nums = sorted(nums, reverse=True)
        pos = nums[0] * nums[1] * nums[2]
        neg = nums[0] * nums[-1] * nums[-2]

        return pos if pos > neg else neg


if __name__ == "__main__":
    x = [1, 2, 3, 4]
    print(Solution().maximumProduct(x))
