class Solution:
    # Time Complexity: O(n)
    # Algorithm: Dynamic Programming
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        ans = [0 for x in range(n)]
        ans[0] = 1
        ans[1] = 2
        for i in range(2, n):
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n-1]