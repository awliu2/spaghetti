class Solution:
    def func(self, s: str) -> str:
        if s is None or s == "":
            return 0
        
        lenS = len(s)
        rv = []


        for i, c in enumerate(s):
            skipNext = False
            counter = 1
            l = i - 1
            r = i + 1

            # expand palindrome when the same letter is next to itself
            # the "core" of the palindrome
            # also takes care of the "even-length" palindrome edge-case
            while r < lenS and c == s[r]:
                r += 1
                counter += 1
        
            # expand palindrome after "core" has been determined
            while 0 <= l and r < lenS and s[l] == s[r]:
                l -= 1
                r += 1
                counter += 2

            if counter >= len(rv):
                rv = s[l + 1: r]
            

        return rv

print(Solution().func("racecar"))
print(Solution().func("akkd"))
print(Solution().func("cbbd"))
print(Solution().func("ccc"))
print(Solution().func("aaaa"))

