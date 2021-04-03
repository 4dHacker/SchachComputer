def to_coordinates(string):
    a = ord(string[0]) - ord("a")
    b = 8 - int(string[1])
    c = ord(string[2]) - ord("a")
    d = 8 - int(string[3])

    if len(string) == 5:
        return a, b, c, d, string[-1]

    return a, b, c, d


def to_text(a, b, c, d, promotion=""):
    string = chr(a + ord("a"))
    string += str(8 - b)
    string += chr(c + ord("a"))
    string += str(8 - d)

    string += promotion

    return string
