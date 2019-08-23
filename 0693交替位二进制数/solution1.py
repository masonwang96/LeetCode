class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)
        if n.find('00') != -1 or n.find('11') != -1:
            return False
        else:
            return True

        # return not ('11' in str(bin(n)) or '00' in str(bin(n)))


if __name__ == "__main__":
    x = 5
    print(Solution().hasAlternatingBits(x))
