'''Problem : MINIMUM OPERATION TO MAKE ARRAY EQUAL '''

#CODE :

class Solution(object):
    def minOperations(self, n):
        return (n//2)*((n+1)//2)
