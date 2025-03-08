# give two string s,t
# find all chars from t in s but in sequence (word, shortest version of sliding window)
# if true return sequence if false return empty string
#
# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"
# #
# Input: s = "xaayaazxyz", t = "xyz"
#
# Output: "xyz"


class Solution:
    def min_window(self, s:str, t:str)->str:
        if t=='':
            return ''

        quantity_t , window = {},{}

        # set in key-value: how many letters in t
        for i in t:
            quantity_t[i] = 1 + quantity_t.get(i,0) # {'e': 1, 'q': 1, 'w': 1};   if {'w': 2} it is collision

        result, result_len = [-1,-1], float('infinity')
        have = 0 # help track sliding window contains all characters from t
        need = len(quantity_t) # total number unique characters in t (except collision)

        left=0
        for right in range(len(s)):
            c=s[right]

            # current sliding window with quantity of characters
            window[c]=1 + window.get(c,0)

            if c in quantity_t and window[c] == quantity_t[c]:
                have+=1 # hove many equality with target (except collision)

            while have == need: # we find result, targeted sliding window
                if (right - left + 1) < result_len: # fide lowest targeted window
                    result = [left, right]
                    result_len = right - left + 1

                window[s[left]] -= 1 # decrease quantity from sliding window

                # check if targeted sliding window contain targeted values
                if s[left] in quantity_t and window[s[left]]< quantity_t[s[left]]:
                    # if not contain, then we should decrease 'have'
                    # as result we lost one element from targeted window
                    # it  is mean have != need
                    have -= 1
                left += 1

        left, right = result
        return s[left: right + 1 ] if result_len != float('infinity') else ''


obj = Solution()
print(obj.min_window('qdddwerrwqret', 'qwe'))
