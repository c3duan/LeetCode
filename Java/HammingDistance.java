class Solution {
    /**
     * Time Complexity: O(n)
     * n = number of digits of z
     */
    public int hammingDistance(int x, int y) {
        int z = x ^ y;
        int count = 0;
        while(z != 0) {
            if ((z & 1) == 1) count += 1;
            z = z >> 1;   
        } 
        return count;
    }
}