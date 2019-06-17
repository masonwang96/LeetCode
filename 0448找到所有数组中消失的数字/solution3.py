class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        res = []
        for i in range(len(nums)):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res


if __name__ == "__main__":
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(x))
