class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        for i in range(len(digits)):
            s += str(digits[i])
        s = str(int(s) + 1)
        return [int(x) for x in s]


if __name__ == "__main__":
    x = [9, 9, 9]
    print(Solution().plusOne(x))
    x = [4, 3, 2, 1]
    print(Solution().plusOne(x))
