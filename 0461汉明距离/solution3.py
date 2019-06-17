class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        ^: 自动二进制异或，并返回十进制值
        """
        return bin(x ^ y).count('1')


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
