# give s string, and k.
# you can change only k times characters in string
# return the length of the longest substring whicch contains only one distinct character
#
# Input: s = "XYYX", k = 2
# Output: 4
#
# Input: s = "AAABABB", k = 1
# Output: 5


class Solution:
    def character_replacement(self, s: str, k : int)-> int:
        characters_count = {}
        result = 0
        left  = 0
        max_frequency = 0

        for right in range(len(s)):
            # count for characters
            characters_count[s[right]] = 1 + characters_count.get(s[right], 0)

            # max frequency for one character
            max_frequency = max(max_frequency, characters_count[s[right]])

            # check if sliding window is invalid for k index distance
            while (right - left + 1) - max_frequency > k:
                # decreasing count for character
                characters_count[s[left]] -=1
                # move forward left point
                left+=1

            # check the max result and left - right +1 consider k value
            result = max(result, right-left+1)
        return result


obj = Solution()
print(obj.character_replacement('ABCACCBBCCAACCC',2))
