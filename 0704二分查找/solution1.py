class Solution:
    def search(self, nums: [int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:  # 要加等号
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1


if __name__ == "__main__":
    x = [-1, 0, 3, 5, 9, 12]
    y = 9
    print(Solution().search(x, y))
