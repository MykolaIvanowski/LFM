

def length_of_last_word(sentence):
    els = sentence.split(" ")
    el = [i for i in els if i != ""]
    return len(el[-1])


print(length_of_last_word("last word"))
print(length_of_last_word(" new last word   "))
print(length_of_last_word("the new last last words     "))


## new solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        world = s.strip().split(' ')[-1]
        return len(world)