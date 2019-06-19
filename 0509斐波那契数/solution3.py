class Solution:
    def fib(self, N: int) -> int:
        return int((5**0.5)*0.2*( ((1+5**0.5)/2)**N-((1-5**0.5)/2)**N))


if __name__ == "__main__":
    x = 3
    print(Solution().fib(x))
