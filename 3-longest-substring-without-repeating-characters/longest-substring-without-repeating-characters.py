class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}  # stores the last seen index of each character
        l = 0
        max_len = 0

        for r, char in enumerate(s):
            if char in last_index and last_index[char] >= l:
                l = last_index[char] + 1  # move left pointer
            max_len = max(max_len, r - l + 1)
            last_index[char] = r  # update last seen index

        return max_len

        