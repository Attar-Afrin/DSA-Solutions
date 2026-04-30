class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        maxi=float('-inf')
        if len(nums)<2:
            return nums[0]
        for i in range(len(nums)):
            total=total+nums[i]
            maxi=max(total,maxi)
            if total<0:
                total=0
            
        
            
        return maxi

        