def convert_to_title(columnNumber):
    title = ""
    while columnNumber:
        columnNumber = columnNumber - 1
        title = chr(columnNumber % 26 + 65) + title
        columnNumber = columnNumber // 26
    return title