class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if not pattern or not str or len(set(str)) != len(set(pattern)) or len(str) != len(pattern):
            return False
        mapping = {}
        for i in range(len(pattern)):
            if pattern[i] in mapping.keys():
                if mapping[pattern[i]] != str[i]:
                    return False
            elif not str[i] in mapping.values():
                mapping[pattern[i]] = str[i]
            else:
                return False

        return True


if __name__ == "__main__":
    p = "abba"
    x = "dog dog dog dog"
    print(Solution().wordPattern(p, x))
