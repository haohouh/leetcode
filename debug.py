class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+1)
        k = [0] * n
        k[0] = 0

        if n == 0 : return 0
        if n == 1 : return 1
        
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1]
            k[i-1] = k[i-2]
            for j in range(1,i):
                if nums[i-j-1] < nums[i-1] and k[i-j-1] == i-j-1 and k[i-j-1] + 1 > k[i-1]:
                    dp[i] = max(dp[i-j]+1,dp[i])
                    k[i-1] = i-1
        return dp[n]
if __name__ == "__main__":
    b = Solution()
    print(b.lengthOfLIS([2,3,7,101,4,5]))