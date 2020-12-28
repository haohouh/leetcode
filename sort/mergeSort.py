'''
mergeSort
the most important part is 
1. in the merge function , you need declare a copy arry , in python, you have to specify [None] * len() and use for loop to assign the value
2. you need to assgin the value back to nums which is line 42, 43
3. O(nlogn) , need O(n) space

归并排序每次递归需要用到一个辅助表，长度与待排序的表相等，虽然递归次数是O(logn)，但每次递归都会释放掉所占的辅助空间，所以下次递归的栈空间和辅助空间与这部分释放的空间就不相关了，因而空间复杂度还是O（n）。
而快速排序每次递归都会返回一个中间值的位置，必须使用栈。所以空间复杂度就是栈用的空间。
'''
def mergeSort(nums,lo,hi):
    if lo >= hi:
        return
    mid = int ((lo+hi) / 2)
    mergeSort(nums,lo, mid)
    mergeSort(nums,mid + 1,hi)
    merge(nums, lo, mid, hi)


def merge(nums, lo, mid, hi):

    copy = [None] * (hi-lo+1)
    for i in range(0,hi-lo+1):
        copy[i] = nums[lo+i] 

    k = 0
    j = mid + 1
    i = lo
    while(k < len(copy)):
        if i > mid:
            copy[k] = nums[j]
            k +=1
            j +=1
        elif j > hi:
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
    for i in range(0,len(copy)):
        nums[lo+i] = copy[i]


if __name__ == "__main__":
    nums = [1,3,2,1,5,6]
    mergeSort(nums,0,5)
    print (nums)
