class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        """
        分析：while B not in A每次判断太费时间，导致超出时间限制。
        """
        cnt = 1
        temp = A
        while B not in A:
            cnt += 1
            A = A + temp
        return cnt


if __name__ == "__main__":
    x = "abcd"
    y = "cdabcdab"
    print(Solution().repeatedStringMatch(x, y))
