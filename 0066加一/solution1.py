class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 不需要了
        # if len(digits) == 1:
        #     if digits[0] + 1 == 10:
        #         return [1, 0]
        #     else:
        #         return [digits[0] + 1]

        digits[-1] += 1
        for i in range(1, len(digits)):
            if digits[-i] == 10:
                digits[-i - 1] += 1
                digits[-i] = 0
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


if __name__ == "__main__":
    x = [9, 9, 9]
    print(Solution().plusOne(x))
    x = [4, 3, 2, 1]
    print(Solution().plusOne(x))
