'''
heapSort
initialize heap o(n),  adjust O(nlogn), storge O(1)
'''

def heapSort(nums):

    for i in range(len(nums)//2 ,-1,-1):
        heapify(nums,i,len(nums))
    
    for i in range(len(nums)-1,-1,-1):
        nums[i],nums[0] = nums[0],nums[i]
        heapify(nums,0,i)

def heapify(nums,i,n):
    
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if (l < n and nums[largest] < nums[l]):
        largest = l
    if ( r < n and nums[largest] < nums[r]):
        largest = r

    if largest != i:
        nums[largest], nums[i] = nums[i], nums[largest]
        heapify(nums,largest,n)

if __name__ == "__main__":
    a = [7,5,6,2,3,1]
    heapSort(a)
    print (a)
    
    
