class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxi=float('-inf')
        while i<j:
            res=min(height[i],height[j])
            final=res*((j-i))
            maxi=max(final,maxi)
            if height[i]>height[j]:
                j-=1
            else:
                i+=1
            
        return maxi

        


        