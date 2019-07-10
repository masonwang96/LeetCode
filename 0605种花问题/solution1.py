class Solution:
    def canPlaceFlowers(self, flowerbed: [int], n: int) -> bool:
        res = 0
        flowerbed = [0] + flowerbed + [0]
        flowerbed = ''.join([str(x) for x in flowerbed]).split('1')
        for s in flowerbed:
            if s:
                res += (len(s) - 1) // 2
            if res >= n:
                return True
        return False


if __name__ == "__main__":
    x = [1, 0, 0, 0, 1]
    y = 1
    print(Solution().canPlaceFlowers(x, y))
