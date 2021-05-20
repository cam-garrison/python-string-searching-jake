import string


# This will create a list of lists of words
tokens = [sub.split() for sub in big_list]


# loop through list of lists
for i in range(len(tokens)):
    for x in range(len(tokens[i])):
        if tokens[i][x] == '':
            continue
        if tokens[i][x] in nameslist:
            wordlist[x] = "name"
