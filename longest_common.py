class Solution:
    def Longest_pre(self , strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for char in strs[1:]:
            while not char.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
'''
prefix = ""
        for char in zip(*strs):
            if len(set(char)) == 1:
                prefix +=char[0]
            else:
                break
        return prefix
'''

sol = Solution()
print(sol.Longest_pre(["flower", "flow", "flight"]))