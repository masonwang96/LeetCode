class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        if len(s) % 2 == 1:
            return False
        pairs = {'(': ')', '{': '}', '[': ']'}
        stack = [s[0]]
        i = 1
        while len(stack) > 0 and i < len(s):
            if stack[-1] not in pairs.keys():
                break
            if pairs[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return True if len(stack) == 0 else False


if __name__ == "__main__":
    x = '()'
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == True)
    x = '()[]{}'
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == True)
    x = ''
    print(Solution().isValid(x))
    assert (Solution().isValid(x) == False)
