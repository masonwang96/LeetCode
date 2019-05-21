def removeDuplicates(nums):
    # nums_new = list(set(nums))
    # print(nums_new)
    # return len(nums_new)
    if len(nums) == 0:
        return 0
    
    last = nums.pop()
    true_last = last
    delete = None
    while(last != delete):
        delete = last
        while(delete in nums):
            nums.remove(delete)
        nums.insert(0, delete)
        if nums[-1] == true_last:
            break
        last = nums.pop()
    return len(nums)

if __name__ == '__main__':
    nums = [1,1,2,3,4,4]
    length = removeDuplicates(nums)
    print(length)