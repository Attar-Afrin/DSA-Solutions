class Solution:
    def check(self, nums: List[int]) -> bool:
        n=len(nums)
        count=1
        if n==1:
            return True
        res=nums*2
        for i in range(1, len(res)):
            if res[i]>=res[i-1]:
                count+=1
            else:
                count=1
            if count==n:
                return True
        return False
        
        