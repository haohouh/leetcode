def bucketSort(nums,a,b):

    result = [0] * (b-a+1)
    for i in nums:
        result[i-a] += 1
    j = 0
    for k in range(0,b-a+1):
        while( result[k] != 0):
            nums[j] = k + a
            result[k] -= 1
            j +=1


if __name__ == "__main__":
    nums = [3,2,2,4,1]
    bucketSort(nums,1,4)
    print (nums)

            
            