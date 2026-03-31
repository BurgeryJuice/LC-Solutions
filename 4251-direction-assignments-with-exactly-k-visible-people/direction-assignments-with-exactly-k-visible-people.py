import math as m 
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        


        return (2*(m.comb(n-1,k)))%((10**9)+7)