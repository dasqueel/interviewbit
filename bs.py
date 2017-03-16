#search for target element t in sorted array a and return t position in array
def binarySearch(a,t):
	left = 0
	right = len(a)-1

	while left <= right:
		mid = (left+right)/2

		if a[mid] == t:
			return mid
		elif a[mid] < t:
			left = mid+1
		else:
			right = mid-1

	return -1

print binarySearch([5, 7, 7, 8, 9, 10],3)
'''class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def findCount(self, A, B):
    	start = 0
    	end = len(A) - 1
    	mid = (start + end) / 2
    	if mid == B
    	return A[mid]


sol = Solution()
print sol.findCount([5, 7, 7, 8, 8, 10],8)'''