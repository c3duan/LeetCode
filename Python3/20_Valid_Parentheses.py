class Solution:
    # Time Complexity: O(n)
    def isValid(self, s: str) -> bool:
        parenth_balance = 0
        p_marks = []
        square_balance = 0
        s_marks = []
        curly_balance = 0
        c_marks = []
        for j in range(len(s)):
            if s[j] == "(":
                parenth_balance += 1
                p_marks.append(j)
                
            if s[j] == "[":
                square_balance += 1
                s_marks.append(j)
            
            if s[j] == "{" :
                curly_balance += 1
                c_marks.append(j)
                
            if s[j] == ")":
                parenth_balance -= 1
                if len(p_marks) == 0 or (j - (p_marks[-1]+1)) % 2 != 0:
                    return False
                p_marks.pop()
            
            if s[j] == "]":
                square_balance -= 1
                if len(s_marks) == 0 or (j - (s_marks[-1]+1)) % 2 != 0:
                    return False
                s_marks.pop()
                
            if s[j] == "}":
                curly_balance -= 1
                if len(c_marks) == 0 or (j - (c_marks[-1]+1)) % 2 != 0:
                    return False
                c_marks.pop()
                
        return parenth_balance == 0 and square_balance == 0 and curly_balance == 0