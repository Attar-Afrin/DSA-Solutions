class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        res=[]
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                res.append(count)
                count=0
        if len(res)>0:
            j=max(res)
            return max(j,count)
        else:
            return count

        