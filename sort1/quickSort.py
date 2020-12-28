def quickSort(nums):
    def helper(nums,low,high):
        if low >= high:
            return
        p = partition(nums,low,high)
        helper(nums,low,p-1)
        helper(nums,p+1,high)
    helper(nums,0,len(nums)-1)

def partition(nums,low,high):
    i = low
    j = low
    while j < high:
        if nums[j] < nums[high]:
            nums[j],nums[i] = nums[i],nums[j]
            i = i + 1
        j = j + 1
    nums[i],nums[high] = nums[high],nums[i]
    return i

if __name__ == "__main__":
    a = [6,5,2,3,1]
    quickSort(a)
    print(a)
        