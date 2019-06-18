class Solution:
    def nextGreaterElement(self, nums1: [int], nums2: [int]) -> [int]:
        d, s = {}, []
        for n in nums2:
            while s and n > s[-1]:
                d[s.pop()] = n
            s.append(n)
        return [d[key] if key in d else -1 for key in nums1]


if __name__ == "__main__":
    x = [4, 1, 2]
    y = [1, 3, 4, 2]
    # x = [2, 4]
    # y = [1, 2, 3, 4]
    print(Solution().nextGreaterElement(x, y))
