''' PROBLEM: Determine if String Halves Are Alike '''


#CODE :

class Solution:
    def halvesAreAlike(self, s):
        check=('aeiouAEIOU')
        t=0
        b=0
        for i in range(len(s)//2):
            if s[i] in check:
                t+=1
            if s[-i-1] in check:
                b+=1
               
        return t==b
