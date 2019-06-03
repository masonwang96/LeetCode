class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(numbers):
            if num in dic:
                return [dic[num] + 1, index + 1]
            dic[target - num] = index


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(numbers, target))
