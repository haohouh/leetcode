"""

一定要传第K个这样 search_1 , search_2 好处理
返回条件 k == 1 或者 有一个长度没了
一定要保证len1 < len2
传l1+ 什么不要忘了
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if (l1 + l2) % 2 == 0:
            a = self.findNumber(nums1,nums2,0,len(nums1)-1, 0 , len(nums2) - 1 , (l1+l2) // 2)
            b = self.findNumber(nums1,nums2,0,len(nums1)-1, 0 , len(nums2) - 1 ,(l1+l2) // 2 + 1)
            return  (a + b) / 2.0
        else:
            return self.findNumber(nums1,nums2,0,len(nums1)-1, 0 , len(nums2) - 1 , (l1+l2) // 2 + 1) 
        
        
    def findNumber(self,num1,num2,l1,h1,l2,h2,k):
        if l1 > h1: return num2[l2 + k - 1]
        if l2 > h2: return num1[l1 + k - 1 ]
        len_1 = h1 - l1 + 1
        len_2 = h2 - l2 + 1
        if len_1 > len_2: return self.findNumber(num2,num1,l2,h2,l1,h1,k)
        search_1 = min(k//2,len_1)
        search_2 = k - search_1
        if k == 1: return min(num1[l1],num2[l2])
        if num1[l1+search_1-1] == num2[l2+search_2-1]:
            return num1[l1+search_1-1]
        elif num1[l1+search_1-1] > num2[l2+search_2-1]:
            return self.findNumber(num1,num2,l1,l1+search_1-1,l2+search_2,h2,k - search_2)
        else:
            return self.findNumber(num1,num2,l1+search_1,h1,l2,l2+search_2-1,k - search_1)
        