class Solution:
    def findErrorNums(self, nums: [int]) -> [int]:
        arr = [1] * len(nums)
        for n in nums:
            arr[n - 1] -= 1
        res = [0, 0]
        for i in range(len(arr)):
            if arr[i] == -1:
                res[0] = i + 1
            if arr[i] == 1:
                res[1] = i + 1
        return res


if __name__ == "__main__":
    x = [1, 2, 2, 4]
    x = [3, 2, 3, 4, 6, 5]
    print(Solution().findErrorNums(x))
