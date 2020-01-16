def find_short(s):
    list_of_words = s.split(" ")
    return min( len(element) for element in list_of_words)

