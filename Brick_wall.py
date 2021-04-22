'''Problem : Brick Wall.py '''

#CODE :

class Solution(object):
    def leastBricks(self, wall):
        widths = collections.defaultdict(int)
        result = len(wall)
        for row in wall:
            width = 0
            for i in range(len(row)-1):
                width += row[i]
                widths[width] += 1
                result = min(result, len(wall) - widths[width])
        return result
