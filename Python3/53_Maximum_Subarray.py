from typing import List

class Solution:
    # Time Complexity: O(n)
    # Algorithm: Dynamic Programming
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp = nums[0]
        max_sum = dp
        for i in range(1, n):                
            add = dp + nums[i]
            dp = max(nums[i], add)
            if dp > max_sum:
                max_sum = dp
             
        return max_sum

    # Time Complexityz: T(n) = 2T(n/2) + O(1) => O(n) (d = 0, a = 2, b = 2)
    # Algorithm: Divide and Conquer
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        mid = int((n-1) / 2)
        L = nums[:mid+1]
        R = nums[mid+1:]
        SL = self.maxSubArray(L)
        SR = self.maxSubArray(R)
        max_left = nums[mid]
        max_right = nums[mid+1]
        
        i = mid
        temp = 0
        while i >= 0:
            temp += nums[i]
            if temp > max_left:
                max_left = temp
            i -= 1
                
        i = mid + 1
        temp = 0
        while i < n:
            temp += nums[i]
            if temp > max_right:
                max_right = temp
            i += 1
            
        return max(SL, SR, max_left + max_right)
