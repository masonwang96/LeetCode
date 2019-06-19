class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        i = 2
        j = num // 2
        while i < j:
            if num % i == 0:
                sum += i
                sum += (num // i)
                j = num // i
            i += 1

        return sum == num


if __name__ == "__main__":
    x = 28
    x = 20996011
    print(Solution().checkPerfectNumber(x))
