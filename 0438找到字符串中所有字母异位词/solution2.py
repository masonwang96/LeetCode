class Solution:
    def findAnagrams(self, s: str, p: str) -> [int]:
        def cmp(a: list, b: list) -> bool:
            for x in a:
                if x not in b:
                    return False
                else:
                    b.remove(x)
            return True

        l = len(p)
        res = []
        for i in range(len(s)):
            temp = s[i:i + l]
            if cmp(list(p), list(temp)):
                res.append(i)
        return res


if __name__ == "__main__":
    x = "cbaebabacd"
    y = "abc"
    # x = "abab"
    # y = "ab"
    print(Solution().findAnagrams(x, y))
