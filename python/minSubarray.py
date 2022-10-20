def minSub(nums, k):
    count = {}
    l, r = 0,  0
    rv = len(nums)
    while r < len(nums):
        count[nums[r]] = count.get(nums[r], 0) + 1
        r += 1
        # print(len(count))
        if len(count) < k:
            continue
        
        while len(count) == k:
            # sub_len is actually (r - 1) - l + 1, 
            # since we incremented r an extra time before entering while loop
            sub_len = r - l 
            # print(f"sublen: {sub_len}")
            rv = min(rv, sub_len)
            if count[nums[l]] == 1:
                count.pop(nums[l])
            else:
                count[nums[l]] -= 1
            l += 1
    if l == 0 and r == len(nums):
        return -1
    return rv


print(minSub([2,2,1,3], 3))

print(minSub([2,2,1,3],1))
print(minSub([2,2,1,3,3,4],4))
print(minSub([1,2,3,4,4,4,4,4,5],5))
print(minSub([1,2,3,4,4,4,4,4,5],2))
