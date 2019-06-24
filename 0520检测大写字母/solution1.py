class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n_diff = 0
        lower = word.lower()
        for i in range(len(word)):
            if not word[i] == lower[i]:
                n_diff += 1
        if n_diff == 0 or n_diff == len(word):
            return True
        if n_diff == 1:
            if word[0].isupper():
                return True
        return False


if __name__ == "__main__":
    x = 'flaG'
    print(Solution().detectCapitalUse(x))
