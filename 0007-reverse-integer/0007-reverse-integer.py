class Solution:
    def reverse(self, x: int) -> int:
        res=0
        flag=1
            
        if x<0:
            flag=0
                
            x=x+(2*(-x))         
        while x>0:
            r=x%10
            res=res*10+r
            x//=10
        if not flag:
            return -res
        else:
            return res
        if res<-2**31 or res>2**31-1:
            return 0
        

        