class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        index1 = {list1[i]: i for i in range(len(list1))}
        index2 = {list2[i]: i for i in range(len(list2))}
        intersection = set(list1) & set(list2)
        sum_index = {r: index1[r] + index2[r] for r in intersection}
        return [r for r in intersection if sum_index[r] == min(sum_index.values())]


if __name__ == "__main__":
    x = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    y = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    y = ["KFC", "Shogun", "Burger King"]
    print(Solution().findRestaurant(x, y))
