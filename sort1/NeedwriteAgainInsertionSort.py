def insertionSort(nums):
    for i in range(len(nums)):
        cur = nums[i]
        j = i
        while j > 0 and cur < nums[j-1]:
            nums[j] = nums[j-1]
            j = j - 1
        nums[j] = cur
    

if __name__ == "__main__":
    a = [7,5,6,2,3,1]
    insertionSort(a)
    print (a)