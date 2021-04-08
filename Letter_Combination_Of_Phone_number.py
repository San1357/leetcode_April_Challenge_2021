''' problem : Letter Combination Of Phone Number ''' 

#code :

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        total = 1
        for digit in digits:
            total *= len(lookup[int(digit)])
        result = []
        for i in range(total):
            base, curr = total, []
            for digit in digits:
                choices = lookup[int(digit)]
                base //= len(choices)
                curr.append(choices[(i//base)%len(choices)])
            result.append("".join(curr))
        return result
