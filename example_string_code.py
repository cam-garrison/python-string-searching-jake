import string


# This will create a list of lists of words
replaced = [sentence.replace(",", "") for sentence in big_list]
tokens = [sub.split() for sub in replaced]


# loop through list of lists
for i in range(len(tokens)):
    for x in range(len(tokens[i])):
        if tokens[i][x] == '':
            continue
        if tokens[i][x] in nameslist:
            wordlist[x] = "name"

    
list_complete_strings = []
for wordlist in tokens:
    complete_string = ''
    for word in wordlist:
        complete_string += word + ' ' 
    list_complete_strings.append(complete_string)

    
