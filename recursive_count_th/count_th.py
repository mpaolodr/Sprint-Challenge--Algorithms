'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # TBC
    i = 0
    j = i + 1

    # base case
    if len(word) == 0 or j == len(word):
        return 0

    elif word[i] == "t" and word[j] == "h":
        return 1 + count_th(word[i + 1:])
    else:
        return 0 + count_th(word[i + 1:])
