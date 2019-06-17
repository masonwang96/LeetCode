class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        r = c = 0
        for n in nums:
            if n:
                c += 1
            else:
                r = max(r, c)
                c = 0
        return max(r, c)


if __name__ == "__main__":
    x = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(x))
