class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[:1].upper() + word[1:].lower() == word:
            return True
        return word.isupper() or word.islower()


if __name__ == "__main__":
    x = 'flaG'
    print(Solution().detectCapitalUse(x))
