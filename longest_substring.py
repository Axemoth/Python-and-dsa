class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            max_length = max(max_length,right-left+1)
        return max_length

s = input("Enter your string: ")
solution = Solution()
result = solution.lengthOfLongestSubstring(s)
print("Length of longest substring without repeating characters is:", result)



        
        