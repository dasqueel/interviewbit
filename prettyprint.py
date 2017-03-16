class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
    	x = []
    	n = 2*A-1
    	mid = A-1
    	for i in range(0,n):
    		for j in range(0,n):
    			x.append([i,j])

    	final = []

    	for c in x:
    		num = max(abs(c[0]-mid),abs(c[1]-mid)) + 1
    		final.append(num)

    	return [final[i:i+n] for i in range(0, len(final), n)]

sol = Solution()
print sol.prettyPrint(3)