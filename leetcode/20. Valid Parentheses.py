class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        op = ["(","{","["]
        cl = [")","}","]"]
        oc = 0
        cc = 0
        for i in s:
            if i in op:
                oc+=1
                brackets.append(i)
            else:
                cc+=1
                try:
                    temp = brackets.pop()
                except:
                    return False
                if temp == op[0]:
                    if i != cl[0]:
                        return False  
                elif temp == op[1]:
                    if i != cl[1]:
                        return False 
                elif temp == op[2]:
                    if i != cl[2]:
                        return False
        if oc == cc:            
            return True
        else:
            return False