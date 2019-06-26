class Solution:
    def findUnsortedSubarray(self, nums: [int]) -> int:
        nums_sort = sorted(nums)
        i, j = 0, 0
        for k in range(len(nums)):
            if nums[k] != nums_sort[k]:
                i = k
                break
        for k in range(len(nums) - 1, 0, -1):
            if nums[k] != nums_sort[k]:
                j = k
                break

        return j - i + 1 if j > i else 0


if __name__ == "__main__":
    x = [2, 6, 4, 8, 10, 9, 15]
    x = [1, 2, 3, 4]
    print(Solution().findUnsortedSubarray(x))
