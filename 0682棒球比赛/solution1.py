class Solution:
    def calPoints(self, ops: [str]) -> int:
        res = 0
        i = 0
        while i < len(ops):
            if ops[i] == 'C':
                # 删除上一轮得分，i自减
                res -= int(ops[i - 1])
                # 删除上一轮得分，i自减
                ops.pop(i)
                ops.pop(i - 1)
                i -= 1
            elif ops[i] == 'D':
                # 加上上一轮2倍，并更新此轮得分到得分列表中
                res += int(ops[i - 1]) * 2
                ops.pop(i)
                ops.insert(i, str(int(ops[i - 1]) * 2))
                i += 1
            elif ops[i] == '+':
                # 判断是否前两轮都存在，并且加上前两轮得分后，更新此轮得分到得分列表中
                if i - 2 >= 0:
                    res += int(ops[i - 1]) + int(ops[i - 2])
                    ops.pop(i)
                    ops.insert(i, str(int(ops[i - 1]) + int(ops[i - 2])))
                else:
                    res += int(ops[i - 1])
                    ops.pop(i)
                    ops.insert(i, str(int(ops[i - 1])))
                i += 1
            else:
                # 数字得分，直接加上去
                res += int(ops[i])
                i += 1
        return res


if __name__ == "__main__":
    x = ["5", "2", "C", "D", "+"]
    x = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(x))
