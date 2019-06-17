class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        l = max(len(x), len(y))
        x, y = x.zfill(l), y.zfill(l)
        return sum([x[i] != y[i] for i in range(l)])


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
