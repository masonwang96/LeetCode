class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        i = 0
        while i < len(nums) - 1:
            if nums[i] >= 1 and nums[i + 1] >= 1:
                nums[i] += nums[i + 1]
                nums.pop(i + 1)
            else:
                i += 1

        return max(nums)


if __name__ == "__main__":
    x = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(x))
