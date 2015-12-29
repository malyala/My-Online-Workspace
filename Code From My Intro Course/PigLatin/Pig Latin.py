def piglatin(string):
    """
    Assumes only words with vowels seperated by spaces
    and only punctuation is at end.
    Returns string sentenece in a form of piglatin.
    """
    if string[-1] in string.ascii_punctuation:
        punc = string[-1]
        string = string[:-1]
    else:
        punc = ''
    strList = string.split(" ")
    ret = ""
    for i in strList:
        ret += pl(i) + " "
    return ret[:-1] + punc


def pl(string):
    maxdepth =len(string)
    return pigl(string, maxdepth)



def pigl(string, numcalls):
    if numcalls == 0:
        raise ValueError("Called with bad args- no vowels in this word: "+ string)
    string = string.lower()
    if string[0] in ['a', 'e', 'i', 'o', 'u']:
        return string + "ay"
    else:
        numcalls -= 1
        return pigl(string[1:]+string[0], numcalls)
    