'''class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0:
            return 0
        if A == 1:
            return 1
        counter = 2
        while counter**2 <= A:
            if counter**2 == A:
                return counter
            else:
                counter += 1
        return counter-1'''


#sol = Solution()
#print sol.sqrt(265376438)


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, n):
        low = 0
        high = n+1
        while high-low > 1:
            print low,high
            mid = (low+high) / 2
            if mid*mid <= n:
                low = mid
            else:
                high = mid
        return low



sol = Solution()
print sol.sqrt(100)