class Solution:
    def arrangeCoins(self, n: int) -> int:
        # if n <= 1:
        #     return n
        k = 1
        while n >= k:
            n -= k
            k += 1
        return k - 1


if __name__ == "__main__":
    x = 5
    x = 1
    print(Solution().arrangeCoins(x))
