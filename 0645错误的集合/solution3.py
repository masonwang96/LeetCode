class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        dup_num = sum(nums) - sum(set(nums))
        drop_num = set(range(1, len(nums) + 1)) - set(nums)
        return [dup_num, drop_num.pop()]


if __name__ == "__main__":
    x = [1, 2, 2, 4]
    x = [3, 2, 3, 4, 6, 5]
    print(Solution().findErrorNums(x))
