# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


# approach-1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res
    

# approach-2
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        indexes = {}
        charset = 0
        for i in range(len(s)):
            index = indexes.get(s[i])
            if index is not None and index >= charset:
                length = i - charset
                charset = index + 1
                if length > l:
                    l = length
            indexes[s[i]] = i
        return max(l, (len(s) - charset))