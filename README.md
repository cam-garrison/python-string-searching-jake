# python-string-searching-jake

Basic Structure of Program:

## setup
- import names as pandas dataframe. 
- convert nameslist to python style list (optional but recommended)

- import data list as pandas df. 
- convert data to python style list (optional)

## loop structure

- for each string in data list

convert to list of words in a python style list (either convert or make as a new column in the dataframe)

- for each word in word list

if word in nameslist:
change to xxx or redacted or whatever

## post loop
assuming all of our words are now converted and are saved in our dataframe

we want to convert our list of words back into proper strings

string = ''
for word in wordlist:
string+= word + ' ' 
