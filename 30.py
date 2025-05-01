"""
LeetCode Problem 30: Substring with Concatenation of All Words

You are given a string `s` and an array of strings `words` of the same length. 
Return all starting indices of substring(s) in `s` that is a concatenation 
of each word in `words` exactly once, in any order, and without any intervening characters.

- The concatenated substring must use all the words in `words` exactly once.
- Each word in `words` has the same length.
- The order of words in the concatenated substring does not matter.

Constraints:
1. `1 <= s.length <= 10^4`
2. `1 <= words.length <= 5000`
3. `1 <= words[i].length <= 30`
4. `s` and `words[i]` consist of lowercase English letters.

Example:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at indices 0 and 9 are "barfoo" and "foobar" respectively.
Both are concatenations of "foo" and "bar".
"""
import itertools
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
            word_len = len(words[0])
            total_len = word_len * len(words)
            word_count = Counter(words)
            result = []

            for i in range(word_len):  # word-aligned sliding windows
                left = i
                curr_count = Counter()
                for j in range(i, len(s) - word_len + 1, word_len):
                    word = s[j:j+word_len]
                    if word in word_count:
                        curr_count[word] += 1

                        # Shrink the window from the left if overused
                        while curr_count[word] > word_count[word]:
                            left_word = s[left:left+word_len]
                            curr_count[left_word] -= 1
                            left += word_len

                        # If all words match
                        if j + word_len - left == total_len:
                            result.append(left)
                    else:
                        curr_count.clear()
                        left = j + word_len

            return result