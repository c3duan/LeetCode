class Solution:
    # Time Complexity: O(n)
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        balance = 0
        i = 0
        for j in range(len(S)):
            if S[j] == "(":
                balance += 1
                
            elif S[j] == ")":
                balance -= 1
                
            if balance == 0:
                res.append(S[i+1:j]) # not including S[i] and S[j]
                i = j+1
                
        return "".join(res)