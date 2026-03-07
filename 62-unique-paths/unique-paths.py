class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = {}

        def pathfinder(a, b):
            if a > m or b > n:
                return 0
            if a == m and b == n:
                return 1
            if (a, b) in mem:
                return mem[(a, b)]
            mem[(a, b)] = pathfinder(a + 1, b) + pathfinder(a, b + 1)
            return mem[(a, b)]

        return pathfinder(1, 1)
