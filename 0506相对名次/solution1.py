class Solution:
    def findRelativeRanks(self, nums: [int]) -> [str]:
        nums_new = nums.copy()
        prize = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        nums_new.sort(reverse=True)
        d = {nums_new[k]: k for k in range(len(nums_new))}
        index = min(3, len(nums_new))
        t = prize[:index]
        t.extend([str(i) for i in range(index+1, len(nums_new)+1)])

        return [t[d[k]] for k in nums]


if __name__ == "__main__":
    x = [5, 4, 3, 2, 1]
    # x = [10, 3, 8, 9, 4]
    print(Solution().findRelativeRanks(x))
