# (int, float, bool, str, tuple, unicode) are immutable.
# Objects of built-in types like (list, set, dict) are mutable.
# Custom classes are generally mutable. To simulate immutability in a class,
#     one should override attribute setting and deletion to raise exceptions.

# int        immutable
# float      immutable
# bool       immutable
# str        immutable
# tuple      immutable
# frozenset  immutable
# bytes      immutable
# complex    immutable


# list       mutable
# set        mutable
# dict       mutable
# bytearray  mutable

# Now comes the question, how do we find out if our
# variable is a mutable or immutable object.
# For this we should understand what ‘ID’ and ‘TYPE’ functions are for.