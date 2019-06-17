class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        licens = ''.join([x for x in S.upper().split('-')])
        extra = len(licens) % K
        res = licens[:extra]

        for i in range(len(licens) // K):
            res += '-' + licens[extra + i * K:extra + (i + 1) * K]

        if not res:
            return res
        if res[0] == '-':
            res = res[1:]

        return res


if __name__ == "__main__":
    x = "5F3Z-2e-9-w"
    y = 4
    # x = "2-5g-3-J"
    # y = 2
    print(Solution().licenseKeyFormatting(x, y))
