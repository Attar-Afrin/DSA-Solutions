class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]==target:
                return True
            if nums[j]==target:
                return True
            i+=1
            j-=1
        return False

        