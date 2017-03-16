class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
    	binStr = '{0:08b}'.format(A)
    	return binStr.count('1')



sol = Solution()
print sol.numSetBits(11)