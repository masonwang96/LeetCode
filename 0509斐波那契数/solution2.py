class Solution:
    def fib(self, N: int) -> int:
        A = [0, 1]
        for i in range(N - 1):
            A.append(A[-1] + A[-2])
        return A[N]


if __name__ == "__main__":
    x = 3
    print(Solution().fib(x))
