'''problems : Remove All Adjacent Duplicates in String II'''

# CODE :

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # This is a dummy value to avoid index error or repeated len checks
        stack = [['#', 0]]

        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return "".join([c*i for c, i in stack])
