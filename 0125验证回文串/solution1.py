class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [w for w in s if w.isalpha()]
        s = ''.join(s)
        if not s:
            return True
        i = 0
        while i <= len(s) / 2:
            if s[i] == s[len(s) - i - 1]:
                i += 1
            else:
                return False
        return True


if __name__ == "__main__":
    x = 'A man, a plan, a canal: Panama'
    print(Solution().isPalindrome(x))
