class Solution:
    def compress(self, chars: [str]) -> int:
        num = 1
        for i in range(len(chars) - 1, 0, -1):
            if chars[i] == chars[i - 1]:
                num += 1
                del (chars[i])
            else:
                if num > 1:
                    chars[i + 1: i + 1] = list(str(num))
                num = 1
        if num > 1:
            chars[1: 1] = list(str(num))
        return len(chars)
        # i = 0
        # flag = 0
        # while i < len(chars) - 1:
        #     if chars[i] == chars[i + 1]:
        #         chars[i + 1] = '2'
        #         i += 1
        #     elif chars[i].isdigit():
        #         if chars[i - 1] == chars[i + 1]:
        #             chars[i] = str(int(chars[i]) + 1)
        #             if int(chars[i]) + 1 >= 10:
        #                 flag = 1
        #             chars.pop(i + 1)
        #         else:
        #             i += 1
        #     else:
        #         i += 1
        # if flag == 1:
        #     i = 0
        #     while i < len(chars):
        #         if chars[i].isdigit():
        #             if int(chars[i]) >= 10:
        #                 temp = chars[i]
        #                 chars[i] = temp[0]
        #                 chars.insert(i + 1, temp[1])
        #                 i += 2
        #             else:
        #                 i += 1
        #         else:
        #             i += 1
        #
        # return len(chars)


if __name__ == "__main__":
    x = ["a", "a", "b", "b", "c", "c", "c"]
    x = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    print(Solution().compress(x))
