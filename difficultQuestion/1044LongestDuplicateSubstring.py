class Solution(object):
    def __init__(self):
        self.prime = 2**62 -1
        self.base = 26
    def longestDupSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = [ ord(c) - ord("a") for c in s]
        l = 0
        r = len(s) - 1
        while l <= r:
            mid = l +  (r - l) // 2
            if self.valid(mid,nums):
                r = mid - 1
            else:
                l = mid + 1
        l = l - 1
        if l == 0 : return ""
        seen1 = set()
        powerLast = pow(26,l,self.prime)
        h = 0
        for i in range(l):
            h = (h * self.base + nums[i]) % self.prime
        seen1.add(h)
        for i in range(l,len(nums)):
            h = (h * self.base + nums[i] - powerLast*nums[i-l]) % self.prime
            if h in seen1:
                return s[i-l+1:i+1]
            else:
                seen1.add(h)
        
        
    def valid(self,l,nums):
        seen = set()
        powerLast = pow(self.base,l,self.prime)
        h = 0
        for i in range(l):
            h = (h * self.base + nums[i]) % self.prime
        seen.add(h)
        for i in range(l,len(nums)):
            h = (h * self.base + nums[i] - powerLast*nums[i-l]) % self.prime
            if h in seen:
                return False
            else:
                seen.add(h)
        return True