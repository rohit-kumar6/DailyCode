class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        dic = {}

        for i in A:
            dic[i] = dic.get(i, 0) + 1

        for i in range(1, len(A) + 2):
            if dic.get(i, 0) == 0:
                return i
