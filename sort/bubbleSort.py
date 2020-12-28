#average O(n2), stable

def bubbleSort(nums):
    for i in range(len(nums),0,-1):
        for j in range(1,i):
            if nums[j-1]> nums[j]:
                nums[j-1],nums[j] = nums[j],nums[j-1]


if __name__ == "__main__":
    
    nums = [4,3,2]
    bubbleSort(nums)
    print (nums)

