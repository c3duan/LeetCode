class Solution:
    # Time Complexity: O(1 + 2 + 2 + 4 + .... + k) = O(n^2), k is the length of the (n-1)th string
    def countAndSay(self, n: int) -> str:
        answer = '1'
        j = 1
        while n > j:
            new = ''
            i = 0
            while i < len(answer):
                count = 1
                while i < len(answer) - 1 and answer[i] == answer[i+1]:
                    count += 1
                    i += 1
                new += (str(count) + answer[i])
                i += 1
                
            answer = new
            j += 1
            
        return answer