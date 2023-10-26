class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        # range m-n+1 is the amount of sliding needed for sliding window to go through the haystack
        for i in range(m - n + 1):
            #  haystack[i:i + n] is the sliding window
            if haystack[i:i + n] == needle:
                return i
            
        return -1
    
