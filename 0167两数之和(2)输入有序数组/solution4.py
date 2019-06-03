class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i in range(len(numbers)):
            n = target - numbers[i]
            if n in data:
                return [data[n], i + 1]
            data[numbers[i]] = i + 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
