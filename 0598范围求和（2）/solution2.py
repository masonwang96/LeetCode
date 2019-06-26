class Solution:
    def maxCount(self, m: int, n: int, ops: [[int]]) -> int:
        if not ops:
            return m * n
        # ms = []
        # ns = []
        # for op in ops:
        #     ms.append(op[0])
        #     ns.append(op[1])
        # return min(ms) * min(ns)

        return min([op[0] for op in ops]) * min([op[1] for op in ops])


if __name__ == "__main__":
    x = 3
    y = 3
    op = [[2, 2], [3, 3]]
    print(Solution().maxCount(x, y, op))
