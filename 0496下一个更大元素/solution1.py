class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        res = []
        for x in nums1:
            index = nums2.index(x)
            for i in range(index + 1, len(nums2) + 1):
                if i == len(nums2):
                    # 找完了还是没找到
                    res.append(-1)
                elif nums2[i] > x:
                    # 找到了
                    res.append(nums2[i])
                    break

        return res


if __name__ == "__main__":
    x = [4, 1, 2]
    y = [1, 3, 4, 2]
    x = [2, 4]
    y = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(x, y))
