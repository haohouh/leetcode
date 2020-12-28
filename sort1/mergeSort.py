def mergeSort(nums,low,high):
    if low >= high: return
    mid = low + (high-low)//2
    mergeSort(nums,low,mid)
    mergeSort(nums,mid+1,high)
    merge(nums,low,mid,high)

def merge(nums,low,mid,high):
    if low >= high: return
    copy = [0] * (high-low+1)
    k = 0
    i = low
    j = mid + 1
    while k < len(copy):
        if i > mid:
            copy[k] = nums[j]
            k += 1
            j += 1
        elif j > high:
            copy[k] = nums[i]
            k += 1
            i += 1
        elif nums[i] < nums[j]:
            copy[k] = nums[i]
            i += 1
            k += 1
        else:
            copy[k] = nums[j]
            j += 1
            k += 1
    
    for i in range(len(copy)):
        nums[low+i] = copy[i]

if __name__ == "__main__":
    a = [6,5,2,3,1]
    mergeSort(a,0,len(a)-1)
    print(a)