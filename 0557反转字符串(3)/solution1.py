class Solution:
    def reverseStr(self, s: str) -> str:
        s = s.split()
        return ' '.join([word[::-1] for word in s])


if __name__ == "__main__":
    x = "Let's take LeetCode contest"
    print(Solution().reverseStr(x))
