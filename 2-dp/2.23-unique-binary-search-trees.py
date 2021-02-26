class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # G(n) = G(0)*G(n-1)+G(1)*G(n-2)+...+G(n-1)*G(0)
        # F(i,n)=G(i−1)⋅G(n−i)
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
