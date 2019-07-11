class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def is_square(x):
            sqrt = x ** 0.5
            if int(sqrt) == sqrt:
                return True
            else:
                return False

        for i in range(int(c ** 0.5) + 1):
            if is_square(c - i ** 2):
                return True
        return False


if __name__ == "__main__":
    x = 4
    print(Solution().judgeSquareSum(x))
