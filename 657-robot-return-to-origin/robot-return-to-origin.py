from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = Counter(moves)
        if moves["U"] == moves["D"] and moves["L"] == moves["R"]:
            return True
        return False