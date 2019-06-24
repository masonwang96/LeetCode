class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse2k(string, k):
            if len(string) < k:
                return string[::-1]
            return string[0:k][::-1] + string[k:]

        i = 0
        if len(s) <= k:
            return s[::-1]
        while i + k < len(s):
            s = s[0:i] + reverse2k(s[i:i + 2 * k], k) + s[i + 2 * k:]
            i += 2 * k

        return s[:i]+s[i:][::-1]


if __name__ == "__main__":
    x = 'abcdefghi'
    k = 2
    print(Solution().reverseStr(x, k))
