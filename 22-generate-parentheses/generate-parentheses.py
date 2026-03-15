class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lis = []
       
        
        def gen(cur,a,b):
            if a==0 and b==0:
                lis.append("".join(cur))
                return
            elif b==a:
                cur.append("(")
                gen(cur,a-1,b)
                cur.pop()
                return
            else:
                cur.append(")")
                gen(cur,a,b-1)
                cur.pop()
                if a!=0:
                    cur.append("(")
                    gen(cur,a-1,b)
                    cur.pop()
                return



            
        gen(["("],n-1,n)
            
        return lis
                