class Solution:
    def substring(self, s):  
        seen = set()
        left = 0
        maximum = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1
            maximum = max(maximum, current_length)
        return maximum

s = "avsgbbcbcbcbcbcbcbc"

h = Solution().substring(s)
print(h)