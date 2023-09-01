

def length_of_last_word(sentence):
    els = sentence.split(" ")
    el = [i for i in els if i!= ""]
    return len(el[-1])


print(length_of_last_word("   fly me   to   the moon  "))