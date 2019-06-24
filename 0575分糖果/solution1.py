class Solution:
    def distributeCandies(self, candies: [int]) -> int:
        return min(len(set(candies)), len(candies) // 2)


if __name__ == "__main__":
    x = [1, 1, 2, 2, 3, 3]
    # x = [1, 1, 2, 3]
    print(Solution().distributeCandies(x))
