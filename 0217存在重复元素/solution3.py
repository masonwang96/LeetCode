class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = {}
        for i in nums:
            # get() 函数返回指定键的值，如果值不在字典中返回默认值。
            dic[i] = dic.get(i, 0) + 1
            if dic[i] > 1:
                return True
        return False


if __name__ == "__main__":
    x = [1, 2, 3, 4, 5, 6, 7]
    print(Solution().containsDuplicate(x))
