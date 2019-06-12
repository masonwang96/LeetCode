class Solution:
    def countSegments(self, s: str) -> int:
        # if not s:
        #     return 0
        # count = 0
        # for i in range(len(s)):
        #     if s[i] != ' ' and s[i + 1] == ' ':
        #         count += 1
        # return count + 1
        # 末尾添加空格
        s += " "
        count = 0
        for i in range(len(s)):
            if s[i] != " " and s[i + 1] == " ":  # 只要前一个字符不是空格且后一个字符是空格就计数一个单词
                count += 1
        return count


if __name__ == "__main__":
    x = "Hello, my name is John"
    print(Solution().countSegments(x))
