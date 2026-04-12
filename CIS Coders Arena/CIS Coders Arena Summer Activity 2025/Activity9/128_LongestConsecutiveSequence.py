
def longestConsecutive( nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return 1
    nums = list(set(nums))
    nums.sort()
    max_len = 1
    curr_len = 1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1] == 1:
            curr_len += 1
        else:
            max_len = max(curr_len,max_len)
            curr_len = 1
    max_len = max(curr_len,max_len)
    
    return max_len 
