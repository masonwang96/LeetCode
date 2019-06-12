class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 先补0
        l = max(len(num1), len(num2))
        num1 = num1.zfill(l)
        num2 = num2.zfill(l)

        res = ''
        carry = 0
        for i in range(l - 1, -1, -1):
            temp = int(num1[i]) + int(num2[i]) + carry
            carry = temp // 10
            res = str(temp % 10) + res

        if carry:
            return '1' + res
        return res


if __name__ == "__main__":
    x = '2'
    y = '3'
    print(Solution().addStrings(x, y))
