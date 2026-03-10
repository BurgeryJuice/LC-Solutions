class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        numst = [int(tokens[0])]
        j = 0
        for i in range(1,len(tokens)):
            if tokens[i][0] == "-" and len(tokens[i])>1:
                numst.append(int(tokens[i]))
                j+=1
                
            elif tokens[i].isalnum():
                numst.append(int(tokens[i]))
                j+=1
                
            else:
                a = numst.pop()
                j-=1
                if tokens[i] == "+":
                    numst[j]+=a
                if tokens[i] == "-":
                    numst[j]-=a
                if tokens[i] == "*":
                    numst[j]*=a    
                if tokens[i] == "/":
                    numst[j] = int(float(numst[j]) / a)
                    
                
        return numst[0]
