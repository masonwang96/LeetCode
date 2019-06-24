class Solution:
    def arrayPairSum(self, nums: [int]) -> int:
        nums.sort()
        return sum(nums[0:-1:2])
        # return sum(nums[::2])


if __name__ == "__main__":
    x = [1, 4, 3, 2]
    print(Solution().arrayPairSum(x))
