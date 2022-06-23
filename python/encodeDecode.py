class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        l = len(strs) - 1
        rv = ""
        for i, s in enumerate(strs):
            for c in s:
                rv += c
                if c == ":":
                    rv += ":;"
            if i < l:
                rv += ":;"
            
        return rv

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        rv = []
        l = len(str) - 1
        skip = 0
        temp = ""
        for i, c in enumerate(str):
            print(temp)
            if i < skip:
                continue
            if c == ":":
                if str[i+1] == ":" and str[i+2] == ";":
                    temp += c
                    skip = i + 2
                if str[i+1] == ";":
                    rv.append(temp)
                    temp = ""
                    skip = i + 2
            else:
                temp += c
            if i == l:
                rv.append(temp)
                temp = ""
        return rv
            

to_encode1 = ["a: ", "b"]
message = "ab::;cd::;e"
message2 = "::;::;"
message3 = "a:::;::;"


#print(Solution().decode(message))
#print(Solution().decode(message2))
#print(Solution().decode(message3))
print(Solution().encode(to_encode1))

print(Solution().decode(Solution().encode(to_encode1)))