class Solution:
    def findRestaurant(self, list1: [str], list2: [str]) -> [str]:
        d = {}
        for i in range(len(list2)):
            if list2[i] in list1:
                d[list2[i]] = i + list1.index(list2[i])
        d = sorted(d.items(), key=lambda d: d[1])
        return [d[i][0] for i in range(len(d) - 1) if d[i][1] == d[0][1]]


if __name__ == "__main__":
    x = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    y = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    y = ["KFC", "Shogun", "Burger King"]
    print(Solution().findRestaurant(x, y))
