class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        max_count=0
        for key,val in d.items():
            if val>max_count:
                max_count=val
                res=key
        return res
        
        