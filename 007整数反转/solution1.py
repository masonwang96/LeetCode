class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        output = ''
        x = str(x)
        if x[0] == '-':
            output += '-'
            x = x[1:]
        # 字符串逆序
        x = str(x)[::-1]
        for i in range(len(x)):
            output += x[i]
        output = int(output)

        return output if -2 ** 31 <= output <= 2 ** 31 - 1 else 0


if __name__ == "__main__":
    x = 123
    print(Solution().reverse(x))
    x = -123
    print(Solution().reverse(x))
    x = 120
    print(Solution().reverse(x))
