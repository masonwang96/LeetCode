class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """
        假设母串S是由子串s重复N次而成， 则 S+S则有子串s重复2N次，
        现在S=ns， S+S=2ns 因此S在S+S[1:-1]中必出现一次以上
        """
        return s in (s + s)[1: - 1]


if __name__ == "__main__":
    x = 'abab'
    print(Solution().repeatedSubstringPattern(x))
