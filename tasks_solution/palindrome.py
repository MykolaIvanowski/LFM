

# my solution
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        arr1 = list(str(x))
        arr2 = arr1[::-1]
        if arr1 == arr2:
            return True
        return False
#     can be shorter!!!
#         if str(x)==str(x)[::-1]:
#             return True
#         return False



# solution without string conversion parshali valid
class Solution:
    # @param x, an integer
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False

        r = 1
        while x / r >= 10:
            r *= 10
        while r > 1:
            divided, x = divmod(x, r)
            x, moduled = divmod(x, 10)
            if divided != moduled:
                return False
            r //= 100

        return True