class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        substring = []
        cnt = 1
        # 统计连续的0和1分别有多少个
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                cnt += 1
            else:
                substring.append(cnt)
                cnt = 1
        # 添加最后一个子串
        substring.append(cnt)

        res = 0
        # 求任意相邻两个数字较小者之和
        for i in range(len(substring) - 1):
            res += min(substring[i], substring[i + 1])

        return res


if __name__ == "__main__":
    x = "00110011"
    x = "00110"
    print(Solution().countBinarySubstrings(x))
