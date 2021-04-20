'''Problem : N Array Tree Preorder Traversal '''

#CODE :

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
	    def solve(root, ans):
		    if root:                          
			    ans.append(root.val)          
			    for child in root.children:   
				    solve(child, ans)
		    return ans
	    return solve(root, [])
