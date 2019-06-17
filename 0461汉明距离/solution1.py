class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x, y = bin(x)[2:], bin(y)[2:]
        l = max(len(x), len(y))
        x, y = x.zfill(l), y.zfill(l)
        count = 0
        for i in range(l):
            if x[i] == y[i]:
                continue
            else:
                count += 1
        return count


if __name__ == "__main__":
    x = 1
    y = 4
    print(Solution().hammingDistance(x, y))
