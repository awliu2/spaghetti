class Solution:
    def func(self, s: str) -> int:
        seen = {}
        rv = 0
        left = 0
        for right in range(len(s)):
            if s[right] in seen:
                if seen[s[right]] < left:
                    rv = max(rv, right - left + 1)
                else:
                    left = seen[s[right]] + 1
            else:
                rv = max(rv, right - left + 1)
            seen[s[right]] = right
            
        return rv

print(Solution().func("abcabcbb"))
print(Solution().func("bbbbb"))
print(Solution().func("pwwkew"))
print(Solution().func(" "))
print(Solution().func("abba"))