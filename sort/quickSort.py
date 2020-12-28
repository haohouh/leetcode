'''
quickSort
line 11 should p-1 and line 12 should be p+1 as p is already in the right place
randrange makes the algorhtim to average ,instead of always using the first or last element
the worst case is O(n2),  use space O(logn)
'''
from random import randrange

def quickSort(nums,lo,hi):

    if (lo >= hi): return
    p = partition(nums,lo,hi)
    quickSort(nums,lo,p-1)
    quickSort(nums,p+1,hi)

def partition(nums,lo,hi):
    x = randrange(lo,hi+1)
    nums[x],nums[hi] = nums[hi],nums[x]
    i = lo
    j = lo
    while (j<hi):
        if nums[j] < nums[hi]:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
        j +=1
    nums[i],nums[hi] = nums[hi],nums[i]
    return i

if __name__ == "__main__":
    nums = [1,3,2,1,5,6,4]
    quickSort(nums,0,6)
    print (nums)    

