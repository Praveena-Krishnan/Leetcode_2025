"""
LeetCode Problem 205: Isomorphic Strings

Description:
Given two strings `s` and `t`, determine if they are isomorphic. Two strings are isomorphic if the characters in `s` can be replaced to get `t`.

Rules:
1. Each character in `s` must map to exactly one character in `t`, and vice versa.
2. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Constraints:
- `s` and `t` consist of any valid ASCII characters.
- The lengths of `s` and `t` are equal.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return True if len(set(zip(s,t)))==len(set(s))==len(set(t)) else False
        