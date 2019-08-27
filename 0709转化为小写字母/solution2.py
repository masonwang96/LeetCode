class Solution:
    def toLowerCase(self, str: str) -> str:
        # 字符串不能修改，先改为list
        str = list(str)
        for i in range(len(str)):
            if 'A' <= str[i] <= 'Z':
                str[i] = chr(ord(str[i]) + 32)
        return ''.join(str)


if __name__ == "__main__":
    x = 'LOVe'
    print(Solution().toLowerCase(x))
