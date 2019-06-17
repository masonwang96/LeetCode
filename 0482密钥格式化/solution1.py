class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper().replace('-', '')
        s = list(s)
        i = len(s)
        while i - k > 0:
            s.insert(i - k, '-')
            i -= k
        return ''.join(s)


if __name__ == "__main__":
    x = "5F3Z-2e-9-w"
    y = 4
    x = "2-5g-3-J"
    y = 2
    print(Solution().licenseKeyFormatting(x, y))
