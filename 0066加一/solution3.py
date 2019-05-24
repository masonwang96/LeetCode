class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits)))
        num += 1
        return list(map(int, list(str(num))))


if __name__ == "__main__":
    x = [9, 9, 9]
    print(Solution().plusOne(x))
    x = [4, 3, 2, 1]
    print(Solution().plusOne(x))
