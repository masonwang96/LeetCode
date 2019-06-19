class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        a = 1
        if num % 2 != 0:
            return False
        for i in range(1, num):
            if num % (2 ** i) == 0:
                a += 2 ** i
                if a == num / (2 ** i):
                    return True
            if num < (2 ** i):
                return False
        return False


if __name__ == "__main__":
    x = 28
    # x = 20996011
    print(Solution().checkPerfectNumber(x))
