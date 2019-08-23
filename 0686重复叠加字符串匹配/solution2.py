class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        当while循环结束后，最多再叠加一次A即为上限，否则不管叠加多少次都一样
        """
        s = ''
        cnt = 0
        """这个while循环判断条件比solution 1简单，节省时间"""
        # 不断叠加A到s，直到s比B长
        while len(s) < len(B):
            s += A
            cnt += 1
        # 此时判断B是否在s中
        if B in s:
            return cnt
        # 不在的话，再叠加一次A，再判断
        s += A
        if B not in s:
            return -1
        else:
            return cnt + 1


if __name__ == "__main__":
    x = "abcd"
    y = "cdabcdab"
    print(Solution().repeatedStringMatch(x, y))
