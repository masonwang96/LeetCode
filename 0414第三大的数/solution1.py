class Solution:
    def thirdMax(self, nums: [int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        s = [min(nums)] * 3
        for x in nums:
            if x in s:
                continue
            elif x > s[0]:
                s.pop(-1)
                s.insert(0, x)
            elif x > s[1]:
                s.pop(-1)
                s.insert(1, x)
            elif x > s[2]:
                s.pop(-1)
                s.insert(2, x)
        return s[-1]


if __name__ == "__main__":
    x = [3, 2, 1]
    x = [2, 2, 3, 1]
    x = [1, -2147483648, 2]
    # x = [5, 2, 4, 1, 3, 6, 0]
    print(Solution().thirdMax(x))
