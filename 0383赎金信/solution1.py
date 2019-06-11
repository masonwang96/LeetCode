class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine = list(magazine)
        i = 0
        while i < len(ransomNote):
            if ransomNote[i] in magazine:
                magazine.remove(ransomNote[i])
                i += 1
            else:
                return False
        return True


if __name__ == "__main__":
    x = 'aa'
    y = 'ab'
    print(Solution().canConstruct(x, y))
