class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_v = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
        max_v = max(max_v,right-left+1)
        return max_v

s = input("Enter your string: ")
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print("Length of longest substring without repeating characters is:", result)



        
        