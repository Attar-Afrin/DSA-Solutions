class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort()
        j=0
        res=0
        res=n*(n+1)//2
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        return abs(sum-res)
            

        