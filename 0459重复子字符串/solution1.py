class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def compose(a: str, b: str) -> bool:
            while b:
                if b[:len(a)] == a:
                    b = b[len(a):]
                else:
                    return False
            return True

        for i in range(len(s) // 2):
            if compose(s[:i + 1], s):
                return True
            else:
                continue
        return False


if __name__ == "__main__":
    x = 'abab'
    print(Solution().repeatedSubstringPattern(x))
