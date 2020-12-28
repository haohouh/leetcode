def BSIndex(nums,lo,hi,target):
    if lo > hi: return -1
    mid = lo + (hi-lo)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return BSIndex(nums,mid+1,hi,target)
    else:
        return BSIndex(nums,lo,mid-1,target)

def BSIndexNonRecur(nums,lo,hi,target):
    if lo > hi: return -1

    mid = lo + (hi-lo)//2

    while (nums[mid] != target and lo <= hi):
        if nums[mid] < target:
            lo = mid + 1
            mid = lo + (hi-lo)//2
        else:
            hi = mid - 1
            mid = lo + (hi-lo)//2
    if nums[mid] == target: return mid
    else:
        return -1



if __name__ == "__main__":
    print(BSIndexNonRecur([1,2,3,4,5,6,7,8],0,6,8))