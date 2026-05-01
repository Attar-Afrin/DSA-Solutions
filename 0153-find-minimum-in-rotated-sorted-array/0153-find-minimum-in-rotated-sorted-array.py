class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        if len(nums)<2:
            return nums[0]
        mini1=float("inf")
        mini2=float('inf')
        res=float('inf')
        while i<=j:
            if nums[i]<mini1:
                mini1=nums[i]
            if nums[j]<mini2:
                mini2=nums[j]
            i+=1
            j-=1
            res=min(mini1,mini2)
        return res

                
             

        