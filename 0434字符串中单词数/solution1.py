class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

if __name__ == "__main__":
    x = "Hello, my name is John"
    print(Solution().countSegments(x))
