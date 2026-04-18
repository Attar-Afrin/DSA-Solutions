class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        res=s.split()
        new=""
        for i in range(len(res)-1,-1,-1):
            if i==0:
                new+=res[i]
            else:
                new+=res[i]+" "
        return new

        