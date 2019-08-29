class Solution:
    def isOneBitCharacter(self, bits: [int]) -> bool:
        bits = bits[:-1]
        num_of_one = 0
        for i in range(len(bits) - 1, -1, -1):
            if bits[i] == 1:
                num_of_one += 1
            else:
                break
        return num_of_one % 2 == 0


if __name__ == "__main__":
    x = [1, 0, 0]
    print(Solution().isOneBitCharacter(x))
