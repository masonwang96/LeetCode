class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)):
            # a = s[0:i]
            # b = s[i + 1:]
            temp = s[0:i] + s[i + 1:]
            if temp == temp[::-1]:
                return True

        return False


if __name__ == "__main__":
    x = 'aba'
    x = 'abca'
    x = 'eccer'
    print(Solution().validPalindrome(x))
