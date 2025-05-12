"""
Problem Description:
LeetCode Problem 10: Regular Expression Matching

The problem is to implement a regular expression matching function with support for '.' and '*'.
- '.' Matches any single character.
- '*' Matches zero or more of the preceding element.

The function should take two inputs:
1. A string `s` representing the text to be matched.
2. A string `p` representing the pattern.

The goal is to determine if the input string `s` matches the pattern `p` entirely.

Constraints:
- Both `s` and `p` consist of only lowercase English letters.
- The pattern `p` may contain the special characters '.' and '*'.
- The matching should cover the entire input string (not partial matching).

The solution should handle edge cases such as:
- Empty strings for `s` or `p`.
- Patterns with consecutive '*' characters.
- Patterns that include '.' or '*' at various positions.
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] in {s[i - 1], '.'}:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2]
                    if p[j - 2] in {s[i - 1], '.'}:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]

        return dp[m][n]

        