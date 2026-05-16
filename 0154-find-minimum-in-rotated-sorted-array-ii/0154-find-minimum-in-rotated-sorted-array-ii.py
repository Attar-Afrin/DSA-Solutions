class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        res=0
        mini=float('inf')
        if len(nums)==1:
            return nums[0]
        while i<=j:
            if nums[i]<nums[j]:
                res=nums[i]
            else:
                res=nums[j]
            mini=min(res,mini)
            i+=1
            j-=1
        return mini

        