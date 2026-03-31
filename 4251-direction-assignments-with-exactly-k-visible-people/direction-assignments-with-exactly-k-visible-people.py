import math as m 
class Solution:
    def countVisiblePeople(self, n: int, pos: int, k: int) -> int:
        pos = 0
        pos+=2*(m.comb(n-1,k))


        return pos%((10**9)+7)