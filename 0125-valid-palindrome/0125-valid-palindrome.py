class Solution:
    def isAlphaNumeric(self,s,i):
        if 97<=ord(s[i])<=122 or 48<=ord(s[i])<=57:
            return True
        else:
            return False
    def isPalindrome(self, s: str) -> bool:
        s=s.strip()
        s=s.lower()
        s=s.replace(" ","")
        i=0
        j=len(s)-1
        while i<j:
            if not self.isAlphaNumeric(s,i):
                i+=1
                continue
            if not self.isAlphaNumeric(s,j):
                j-=1
                continue 
            
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

        