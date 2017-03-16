class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        x = []
        for i in A: x = x + i
        x = sorted(x)
        return x[len(x)/2]


sol = Solution()
A = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]
print sol.findMedian(A)