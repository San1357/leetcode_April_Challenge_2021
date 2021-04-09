'''Problem : VERIFYING AN ALIEN DICTIONARY'''

#CODE :

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                if order.index(words[i][j]) < order.index(words[i+1][j]):
                    break
                elif order.index(words[i][j]) == order.index(words[i+1][j]):
                    if j == min(len(words[i]), len(words[i+1])) - 1:
                        if len(words[i]) - len(words[i+1]) > 0:
                            return False
                        else:
                            continue
                    continue
                else:
                    return False
        return True
