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

# run all at once    
list_complete_strings = []
for wordlist in tokens:
    complete_string = ''
    for word in wordlist:
        complete_string += word
        complete_string += ' '
    list_complete_strings.append(complete_string)

# run to test
list_complete_strings = []
for x in range(len(tokens)):
    wordlist = tokens[x]
    complete_string = ''
    for word in wordlist:
        complete_string += word
        complete_string += ' '
    list_complete_strings.append(complete_string)

    
# changing nameslist to lower with no punctation
for x in range(len(peoples_names)):
        name = peoplesnames[x].translate(
            str.maketrans('', '', string.punctuation))
        peoples_names[x] = name

name_list = [t.lower() for t in peoples_names]
