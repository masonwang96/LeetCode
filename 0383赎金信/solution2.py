class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return all([magazine.count(x) >= ransomNote.count(x) for x in set(ransomNote)])


if __name__ == "__main__":
    x = 'aa'
    y = 'ab'
    print(Solution().canConstruct(x, y))
