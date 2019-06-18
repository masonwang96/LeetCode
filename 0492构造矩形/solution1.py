class Solution:
    def constructRectangle(self, area: int) -> [int]:
        sqrt = int(area ** 0.5)
        while sqrt > 0:
            if area % sqrt == 0:
                return [area // sqrt, sqrt]
            else:
                sqrt -= 1


if __name__ == "__main__":
    x = 3
    print(Solution().constructRectangle(x))
