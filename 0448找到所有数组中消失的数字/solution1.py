class Solution:
    def findDisappearedNumbers(self, nums: [int]) -> [int]:
        n = len(nums)
        res = []
        for i in range(1, n+1):
            if i not in nums:
                res.append(i)

        return res


if __name__ == "__main__":
    x = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(x))
