class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        i = 0
        res = []
        while i < len(nums):
            if nums[i] == i+1 or nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
        for i in range(len(nums)):
            if (i+1) != nums[i]:
                res.append(i+1)

        print('00')


if __name__ == "__main__":
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(x))
