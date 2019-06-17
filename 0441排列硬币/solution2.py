class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n <= 1:
            return n
        for i in range(1, n):
            if sum(range(1, i + 1)) > n:
                return i - 1

        # while sum(range(k)) < n:
        #     t = sum(range(1, k + 1))
        #     k += 1
        # return k - 2


if __name__ == "__main__":
    x = 5
    # x = 8
    print(Solution().arrangeCoins(x))
