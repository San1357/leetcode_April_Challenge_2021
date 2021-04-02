'''Problem : ONES AND ZEROES '''

#CODE :

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.helper(strs, m, n, 0)
    
    def helper(self, strs, m, n, idx):
        if idx == len(strs):
            return 0
        take_curr_str = -1
        count0, count1 = strs[idx].count('0'), strs[idx].count('1')
        if m >= count0 and n >= count1:
            take_curr_str = max(take_curr_str, self.helper(strs, m - count0, n - count1, idx + 1) + 1)
        not_take_curr_str = self.helper(strs, m, n, idx + 1)
        return max(take_curr_str, not_take_curr_str)
        
        
        #    or
        
        
 class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        table = {k:[[0]*(n+1) for _ in range(m+1)] for k in range(len(strs)+1)}
        for i in range(1, len(strs)+1):
            zeroes, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    if j >= zeroes and k >= ones:
                        table[i][j][k] = max(table[i-1][j][k], 1+table[i-1][j-zeroes][k-ones])
                    else:
                        table[i][j][k] = table[i-1][j][k]
        return table[len(strs)][m][n]

