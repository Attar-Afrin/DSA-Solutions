class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        m=len(nums1)
        n=len(nums2)
        if m==1 and n==1:
            nums1[0]=nums2[0]
        
        for i in range(0,len(nums1)):
            if i==(m-n):
                for j in range(len(nums2)):
                    nums1[i]=nums2[j]
                    i+=1
                break
                
            

            

        nums1.sort()   
        return nums1
            

                
        