class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = {i + 1: numbers[i] for i in range(len(numbers))}
        for i, num in enumerate(numbers):
            if s.get(target - num) is not None:
                return [i + 1, s[target - num]]


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
