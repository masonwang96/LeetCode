class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.find('LLL') == -1 and s.count('A') <= 1:
            return True
        return False


if __name__ == "__main__":
    x = 'PPALLP'
    print(Solution().checkRecord(x))
