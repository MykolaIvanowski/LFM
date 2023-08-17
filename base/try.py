# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         res = 0
#         num1, num2 = num1[::-1], num2[::-1]
#         for i1, d1 in enumerate(num1):
#             for i2, d2 in enumerate(num2):
#                 res += (ord(d1) - ord('0')) * (ord(d2) - ord('0')) * 10**(i1+i2)
#         return str(res)
#
#
#
# mult  = Solution()
#
# print(mult.multiply("1212","2121"))


# import requests
#
# s = requests.Session()
#
# print(s)


year = 1650

max_fertile_year = 800
max_birth = int(max_fertile_year * 12 / 9)
max_couple = int(max_birth/2)
people = max_fertile
nex_gen = max_couple * max_birth
