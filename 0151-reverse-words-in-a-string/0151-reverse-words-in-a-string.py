class Solution(object):
    def reverseWords(self, s):
        
        i=len(s)-1
        
        array = []
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break

            j=i
            while i>=0 and s[i]!=" ":
                i-=1

            array.append(s[i+1:j+1])
        
        return " ".join(array)