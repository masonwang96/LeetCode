class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        nums_len = len(nums)
        if nums_len <= 1:
            return False

        nums_dict = {}
        for i in range(nums_len):
            if nums[i] in nums_dict:
                if i - nums_dict[nums[i]] <= k:
                    return True
            nums_dict[nums[i]] = i
        return False


if __name__ == "__main__":
    x = [1, 0, 1, 1]
    k = 1
    print(Solution().containsNearbyDuplicate(x, k))
