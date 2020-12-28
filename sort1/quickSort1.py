from random import randrange
class Solution(object):
    def quickSort(self,num,l,r):
        if l >= r: return num
        p = self.partition(num,l,r)
        self.quickSort(num,l,p-1)
        self.quickSort(num,p+1,r)
        return num


    def partition(self,num,l,r):
        if l >= r: return
        switchIndex = randrange(l,r+1)
        num[r],num[switchIndex] = num[switchIndex],num[r]
        i = l
        j = l
        while j < r:
            if num[j] <= num[r]:
                num[j],num[i] = num[i],num[j]
                i = i + 1
            j = j + 1
        num[i],num[r] = num[r],num[i]
        return i


if __name__ == "__main__":
    s2 = Solution()
    num = [4,2,3,1,6,101,1,3]
    print(num)
    print(s2.quickSort(num,0,len(num)-1))