class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(c ** 0.5)
        i = 0
        while i <= j:
            total = i * i + j * j
            if total > c:
                j = j - 1
            elif total < c:
                i = i + 1
            else:
                return True
        return False


if __name__ == "__main__":
    x = 4
    print(Solution().judgeSquareSum(x))
