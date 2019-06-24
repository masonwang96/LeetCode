class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.upper() == word or word.lower() == word or word.title() == word

        # return word.islower() or word.isupper() or word.istitle()


if __name__ == "__main__":
    x = 'flaG'
    print(Solution().detectCapitalUse(x))
