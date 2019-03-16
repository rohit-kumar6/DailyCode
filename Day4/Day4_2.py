class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):

        n = len(A) // 3
        dic = {}
        for i in A:
            count = dic.get(i, 0) + 1
            if count > n:
                return i
            dic[i] = count

        return -1