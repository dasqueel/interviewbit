class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
    	A = list(set(A))
    	smallest = A[0] ^ A[1]
    	i = 0
    	while i < 15:
    		j = i+1
    		while j < 15:
    			tmp = A[i] ^ A[j]
    			if tmp < smallest:
    				smallest = tmp
    			j += 1
    		i +=1
    	return smallest

sol = Solution()
print sol.findMinXor([0,4,7,9])