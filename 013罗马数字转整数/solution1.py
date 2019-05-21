class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = roman[s[0]]
        for i in range(1, len(s)):
            if roman[s[i - 1]] >= roman[s[i]]:
                result += roman[s[i]]
            else:
                result = result - roman[s[i-1]] + (roman[s[i]]-roman[s[i-1]])
        return result


if __name__ == "__main__":
    x = "MCMXCIV"
    assert (Solution().romanToInt(x) == 1994)
    x = 'LVIII'
    assert (Solution().romanToInt(x) == 58)
