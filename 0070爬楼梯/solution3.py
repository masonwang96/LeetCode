class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == "__main__":
    x = '1111'
    y = '1111'
    print(Solution().addBinary(x, y))
    x = '1010'
    y = '1011'
    print(Solution().addBinary(x, y))
