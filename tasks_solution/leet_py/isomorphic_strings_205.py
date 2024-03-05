def is_isomorphic(s,t):
    if len(s) != len(t):
        return False

    struct1, struct2 = {},{}

    for i in range(len(t)):
        if ((s[i] in struct1 and struct1[s[i]] != t[i]) or
                (t[i] in struct2 and struct2[t[i]] != s[i])):
            return False
        struct1[s[i]] = t[i]
        struct2[t[i]] = s[i]
    return True



print(is_isomorphic('egg','add'))

