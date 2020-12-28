def bubbleSort(nums):
    for i in range(len(nums)-1,-1,-1):
        for j in range(0,i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]

if __name__ == "__main__":
    a = [4,3,2]
    bubbleSort(a)
    print(a)