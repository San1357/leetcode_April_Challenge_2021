'''Problem : Power Of Three '''

#CODE :

class Solution(object):
    def isPowerOfThree(self, n):
        power=3**100;
        if(n<=0):
            return False;
        else:
           if(power%n==0):
              return True;
           else:
              return False;
 
