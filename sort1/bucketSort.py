def bucketSort(nums):
    minNum = min(nums)
    maxNum = max(nums)
    res = [0] * (maxNum-minNum+1)
    for num in nums:
        res[num-minNum] +=1
    k = 0
    for i in range(len(res)):
        while res[i] != 0:
            nums[k] = minNum+i
            k = k + 1
            res[i] -= 1

if __name__ == "__main__":
    a = [7,5,4,1,3]
    bucketSort(a)
    print(a)
            