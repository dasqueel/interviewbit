class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
    	rev = bin(A)[2:]
    	numOfZeros = 32-len(rev)
    	newBitStr = '0'*numOfZeros+rev
    	newBitStr = '0b'+newBitStr[::-1]
    	#return int('newBitStr', 2)
    	return int(newBitStr,2)


sol = Solution()
print sol.reverse(3)