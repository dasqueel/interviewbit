class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if len(A) <= 1:
            return 0
        d = {}

        for i in A:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1

        if B == 0:
            for k,v in d.iteritems():
                if v > 1:
                    return 1
                return 0
        else:
            for k,v in d.iteritems():
                if k-B in d.keys():
                    return 1
            return 0
sol = Solution()
print sol.diffPossible([ 1, 5 ],4)