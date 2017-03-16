'''
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
'''
'''

int i=0;
int j=N-1;

while (i < N && j >= 0)
{
  if (matrix[i][j] == searchEle)
    return true;
  if (matrix[i][j] < searchEle)
    i++;
  else 
    j--;
}
return false;

'''
class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
    	i = 0
    	j = len(A[0])-1

    	while i < len(A[0]) and j >= 0:
    		if A[i][j] == B:
    			return 1
    		if A[i][j] < B:
    			i += 1
    		else:
    			j -= 1
    	return 0

'''class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
    	leftList = 0
    	rightList = len(A) - 1
        numLists = len(A)
        midListIdx = numLists/2
        midList = A[midListIdx]

        while leftList <= rightList:
	        if B == midList[0]:
	        	return 1
	        elif midList[0] < B:
	        	leftList = midList[midListIdx+1]
	        else:
	        	rightList = midList[midListIdx-1]
		return leftList
'''
A = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
sol = Solution()
print sol.searchMatrix(A,3)