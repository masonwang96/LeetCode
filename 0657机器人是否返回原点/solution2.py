class Solution:
    def judgeCircle(self, moves: str) -> bool:
        match = {'R': 1, 'L': -1, 'U': 2, 'D': -2}
        print(sum(match[s] for s in moves))
        return sum(match[s] for s in moves) == 0


if __name__ == "__main__":
    x = "UD"
    # x = "LLL"
    print(Solution().judgeCircle(x))
