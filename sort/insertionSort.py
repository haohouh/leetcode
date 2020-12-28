#Insertion Sort
#insertion sort is not switch, just insert to the position, it will need move the element 1 step back in order to insert
# take some time on line 9 , current < nums[j-1]
#average O(n2), stable

def insertionSort(nums):
    for i in range(1,len(nums)):
        j = i
        current = nums[j]
        while( j > 0 and current < nums[j-1]):
            nums[j] = nums[j-1]
            j -= 1
        nums[j] = current
s = "abc"
"ab".replace("a","c")        
                


if __name__ == "__main__":
    nums = [5,4,3,2,1]
    insertionSort(nums)
    print(nums)



import math
if __name__ == "__main__":
    k = 3 + math.sqrt(5)
    res = 1
    for i in range(40):
        res = res * k
        print (res % 10000)



    k = 3 - 