class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        j=0
        res=[]
        for i in range(len(nums)):

            if nums[j]!=nums[i]:
                nums[j+1]=nums[i]
                j+=1

         
            
        return j+1
                





        
        