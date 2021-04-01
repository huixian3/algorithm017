class Solution(object):
    # 最长回文子串
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # dp[i][j] 表示i-j是否为回文串
        # dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
        # 其中 dp[i][i] = True, dp[i][i+1] = s[i]==s[i+1]

        n = len(s)
        if n <= 1: return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        res = s[0]
        for i in range(n-1, -1, -1): # 该行必须逆序，否则dp[i+1][] 取值为False
            for j in range(i, n):
                # 边界1 处理
                if j == i:
                    dp[i][j] = True
                # 边界2
                elif j == i+1:
                    dp[i][j] = s[i]==s[j]
                # 状态转移方程
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                res = s[i:j+1] if dp[i][j] and j-i+1 > len(res) else res

        return res
# java
    '''
class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length(), n = text2.length();
        int[][] dp = new int[m + 1][n + 1]; 
        for(int i = 1; i <= m; i++){
            for(int j = 1; j <= n; j++){
                if(text1.charAt(i - 1) == text2.charAt(j - 1)){
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                }else{
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][n];
    }
}
'''

# C++
'''
class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, 0));
        for (int i = 1; i <= text1.size(); i++) {
            for (int j = 1; j <= text2.size(); j++) {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[text1.size()][text2.size()];
    }
};

'''
