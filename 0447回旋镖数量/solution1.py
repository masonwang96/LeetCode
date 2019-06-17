class Solution:
    def numberOfBoomerangs(self, points: [[int]]) -> int:
        def dist(a: [[int]], b: [[int]]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2  # ** 0.5

        count = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    if dist(points[i], points[j]) == dist(points[i], points[k]):
                        count += 2
                    if dist(points[j], points[i]) == dist(points[j], points[k]):
                        count += 2
                    if dist(points[k], points[j]) == dist(points[k], points[i]):
                        count += 2
        return count


if __name__ == "__main__":
    x = [[0, 0], [1, 0], [2, 0]]
    print(Solution().numberOfBoomerangs(x))
