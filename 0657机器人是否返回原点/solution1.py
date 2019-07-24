class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # match = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}
        if moves.count('U') == moves.count('D') and moves.count('R') == moves.count('L'):
            return True
        else:
            return False


if __name__ == "__main__":
    x = "UD"
    x = "LLL"
    print(Solution().judgeCircle(x))
