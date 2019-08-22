class Solution:
    def calPoints(self, ops: [str]) -> int:
        scores = []
        for i in ops:
            length = len(scores)

            if i == 'C':
                scores.pop(length - 1)
            elif i == 'D':
                score = scores[length - 1] * 2
                scores.append(score)
            elif i == '+':
                score = scores[length - 2] + scores[length - 1]
                scores.append(score)
            else:
                scores.append(int(i))

        return sum(scores)


if __name__ == "__main__":
    x = ["5", "2", "C", "D", "+"]
    x = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(Solution().calPoints(x))
