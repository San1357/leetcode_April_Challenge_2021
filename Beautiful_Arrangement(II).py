''' PROBLEM : BEAUTIFUL ARRANGEMENT II '''

#CODE : 

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans, a, z = [0] * n, 1, k + 1
        for i in range(k+1):
            if i % 2:
                ans[i] = z
                z -= 1
            else:
                ans[i] = a
                a += 1
        for i in range(k+1,n):
            ans[i] = i + 1
        return ans
