#with three elements in the list, find closest sum to target
#possibly remove 4+ repeats
#find every permutation of trips in l
def target(l,t):
	i = 0
	while i < len(l):

'''from itertools import *
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

def target(l,t):
	closest = 999999999
	closestSum = None
	coms = list(combinations(l,3))
	for com in coms:
		dif = abs(t - sum(com))
		if dif == 0:
			return 0
			break
		else:
			if dif < closest:
				closest = dif
				closestSum = sum(com)
	return closestSum

#print target([-1,2,-4,1],1)

from itertools import *
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def combinations(iterable, r):
        pool = tuple(iterable)
        n = len(pool)
        for indices in permutations(range(n), r):
            if sorted(indices) == list(indices):
                yield tuple(pool[i] for i in indices)
    def threeSumClosest(self, A, B):
    	closest = 999999999
    	closestSum = None
    	coms = list(combinations(A,3))
    	for com in coms:
    		dif = abs(B - sum(com))
    		if dif == 0:
    			return B
    			break
    		else:
    			if dif < closest:
    				closest = dif
    				closestSum = sum(com)
    	return closestSum

sol = Solution()
print sol.threeSumClosest([-1,2,-4,1],1)'''

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        n = len(A)
        if n == 0:
            return B
        A.sort()
        minDiff = 2147483648
        ret = 0
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k :
                temp = A[i]+A[j]+A[k]
                diff = abs(temp-B)
                if diff == 0:
                    return temp
                if diff < minDiff:
                    minDiff = diff
                    ret = temp
                if temp <= B:
                    j += 1
                else:
                    k -= 1
        return ret