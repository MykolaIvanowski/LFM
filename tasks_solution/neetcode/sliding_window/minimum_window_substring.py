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
            quantity_t[i] = 1 + quantity_t.get(i,0) # {'e': 1, 'q': 1, 'w': 1}

        result, result_len = [-1,-1], float('infinity')
        have = 0 # help track sliding window contains all characters from t
        need = len(quantity_t) # total number in unique characters in t

        left=0
        for right in range(len(s)):
            c=s[right]
            window[c]=1 + window.get(c,0)

            if c in quantity_t and window[c] == quantity_t[c]:
                have+=1

            while have==need:
                if (right-left+1)< result_len:
                    result= [left, right]
                    result_len= right-left+1

                window[s[left]] -= 1

                if s[left] in quantity_t and window[s[left]]< quantity_t[s[left]]:
                    have -=1
                left+= 1

        left, right = result
        return s[left: right+1]if result_len != float('infinity') else ''


obj = Solution()
print(obj.min_window('qdddwerrwqret', 'qwe'))
