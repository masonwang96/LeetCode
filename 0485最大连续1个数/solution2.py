class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        a = ''.join(map(str, nums))
        b = ''.join(map(str, nums)).split('0')
        c = max(''.join(map(str, nums)).split('0'))
        return len(max(''.join(map(str, nums)).split('0')))

if __name__ == "__main__":
    x = [1, 1, 0, 1, 1, 1]
    print(Solution().findMaxConsecutiveOnes(x))
