class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        i, j = 0, len(s) - 1
        while i < j:
            if s[i] in vowel and s[j] in vowel:
                s[i], s[j] = s[j], s[i]
                i, j = i + 1, j - 1
            elif not s[i] in vowel:
                i += 1
            else:
                j -= 1

        return ''.join(s)


if __name__ == "__main__":
    x = 'a.'
    print(Solution().reverseVowels(x))
