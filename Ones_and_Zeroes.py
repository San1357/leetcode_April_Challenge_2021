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
        
