class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # l = len(s)
        # s = [s[l-1-i] for i in range(l)]
        #
        # s = s[::-1]

        i, j = 0, len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1

        return s


if __name__ == "__main__":
    x = ["h", "e", "l", "l", "o"]
    print(Solution().reverseString(x))
