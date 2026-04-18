class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    
        n=len(nums)
        j=0
        count=0
        for i in range(0,n):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
                count+=1
        l=n-count
        for i in range(l):
            nums[j]=0
            j+=1
                
        return nums











        """
        Do not return anything, modify nums in-place instead.
        """
        