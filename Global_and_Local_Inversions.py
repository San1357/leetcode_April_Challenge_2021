'''Problem : GLOBAL AND LOCAL INVERSIONS '''

#CODE :

class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(abs(v-i) <= 1 for i,v in enumerate(A))
