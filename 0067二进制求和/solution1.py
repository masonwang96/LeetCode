class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s = ''
        c = '0'
        l = max(len(a), len(b))
        a = a.zfill(l)  # 补齐0
        b = b.zfill(l)
        for i in range(l - 1, -1, -1):
            temp = int(a[i]) + int(b[i]) + int(c)
            c = 0
            if temp >= 2:
                s = str(temp % 2) + s
                c = '1'
            else:
                s = str(temp) + s
        return '1' + s if c == '1' else s


if __name__ == "__main__":
    x = '1111'
    y = '1111'
    print(Solution().addBinary(x, y))
    x = '1010'
    y = '1011'
    print(Solution().addBinary(x, y))
