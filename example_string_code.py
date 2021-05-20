import string


# This will create a list of lists of words
tokens = [sub.split() for sub in big_list]

# loop through list of lists
for wordlist in tokens:
    for x in range(len(wordlist)):
        if wordlist[x] == '':
            continue
        if wordlist[x] in nameslist:
            wordlist[x] = "name"
