class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        d = {i: 0 for i in range(m * n)}
        for op in ops:
            for i in range(op[0]):
                for j in range(op[1]):
                    d[i * m + j] += 1
        d = {d[i]: i for i in d.keys()}

        return d[max(d.keys())]


if __name__ == "__main__":
    x = 3
    y = 3
    op = [[2, 2], [3, 3]]
    print(Solution().maxCount(x, y, op))
