class Solution:
    def findRelativeRanks(self, nums: [int]) -> [str]:
        nums_sorted = sorted(nums, reverse=True)
        # rs=["Gold Medal", "Silver Medal", "Bronze Medal"]

        rs = []
        dic = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}
        for i in range(nums.__len__()):
            tmp_index = nums_sorted.index(nums[i])
            if tmp_index in dic.keys():
                rs.append(dic[tmp_index])
            else:
                rs.append(str(tmp_index + 1))
        return rs


if __name__ == "__main__":
    x = [5, 4, 3, 2, 1]
    x = [10, 3, 8, 9, 4]
    print(Solution().findRelativeRanks(x))
