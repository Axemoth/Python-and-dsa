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
'''zip(*["flower", "flow", "flight"])
→ gives an iterator over:

arduino
Copy code
('f', 'f', 'f')
('l', 'l', 'l')
('o', 'o', 'i')
('w', 'w', 'g')
'''

sol = Solution()
print(sol.Longest_pre(["flower", "flow", "flight"]))