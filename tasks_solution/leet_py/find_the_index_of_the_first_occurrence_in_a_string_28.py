def str_str(haystack,needle):
    if len(needle) == 0:
        return 0
    return haystack.find(needle)