class Solution:
    # Time Complexity: O(m + n)
    # Note: m = len(J), n = len(S)
    def numJewelsInStones(self, J: str, S: str) -> int:
        if len(J) == 0 or len(S) == 0:
            return 0
        
        count = 0
        alpha = list(J) + list(S)
        jew_dict = dict.fromkeys(alpha, 0)
        for s in S:
            jew_dict[s] += 1
        for j in J:
            count += jew_dict[j]
        return count