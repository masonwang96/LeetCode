class Solution:
    def numberOfBoomerangs(self, points: [[int]]) -> int:
        dist_dict = {}  # 相同距离出现的次数
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    dist = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
                    if dist not in dist_dict:
                        dist_dict[dist] = 1
                    else:
                        res += 2 * dist_dict[dist]  # 如果数量增加1，结果增加2n
                        dist_dict[dist] += 1
            dist_dict = {}
        return res

        result = 0
        for m in points:
            dic = {}
            for j in points:
                distance = (m[0] - j[0]) ** 2 + (m[1] - j[1]) ** 2
                dic[distance] = dic.get(distance, 0) + 1
            for val in dic.values():
                if val >= 2:
                    result += val * (val - 1)
        return result


if __name__ == "__main__":
    x = [[0, 0], [1, 0], [2, 0]]
    print(Solution().numberOfBoomerangs(x))
