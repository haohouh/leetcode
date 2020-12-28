def heapSort(nums):
    #build heap
    #the best parameter in heapify is len(nums), not len(nums) -1 
    for i in range(len(nums)//2,-1,-1):
        heapify(nums,i,len(nums))
    
    for i in range(len(nums)-1,-1,-1):
        nums[i],nums[0] = nums[0],nums[i]
        heapify(nums,0,i)


def heapify(nums,i,n):
    if i >= n: return
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if (l < n and nums[l] > nums[largest]):
        largest = l
    if (r < n and nums[r] > nums[largest]):
        largest = r
    
    if largest != i:
        nums[i],nums[largest] = nums[largest],nums[i]
        heapify(nums,largest,n)


if __name__ == "__main__":
    a = [6,5,3,4,1,-1,4,6]
    heapSort(a)
    print(a)