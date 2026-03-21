class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        i = 0
        lb = points[0][0]
        up = points[0][1]
        c = 1
        while i < len(points):
            a = points[i][0]
            b = points[i][1]
            if a>up:
                c+=1
                lb = a
                up = b
            elif a<up:
                if a>lb:
                    lb = a
                if b<up:
                    up = b
            i+=1

        return c