class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<=j:
            if target==nums[i]:
                return i
            if target==nums[j]:
                return j
            i+=1
            j-=1
        return -1

        