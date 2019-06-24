from typing import List

class Solution:
    # Time Analysis: O(n) + O(3^n * 4 ^m) = O(3^n * 4^m)
    # Note: k = len(digits), n = number of digits mapped to 3 digits,
    # m = number of digits mapped to 4 digits, m + n = k
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "" or digits == "0":
            return []
        mapper = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        symbols = []
        for digit in digits:
            symbols.append(mapper[digit])
        return self.product(symbols)
        
    # Time Analysis: O(n + 2 * (3^n * 4^m)) = O(3^n * 4^m)
    def product(self, args: List[str]) -> List[str]:
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = list(map(tuple, args)) # O(n)
        result = [[]]
        ans = []
        
        # Geometric series
        # O(3^n * 4^m)
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        # O(3^n * 4^m)
        return [''.join(prod) for prod in result]
        