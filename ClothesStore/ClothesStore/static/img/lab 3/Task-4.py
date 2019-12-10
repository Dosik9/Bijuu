#Task4
import json
from difflib import get_close_matches
js_on=open("dict.json")
open_f=json.load(js_on)
def Dictionary(word):
    word=word.lower()
    if word in open_f:
        return open_f[word]
    elif word.title() in open_f:
        return open_f[word.title()]
    elif word.upper() in open_f:
        return open_f[word.upper()]
    elif len(get_close_matches(word, open_f.keys()))>0:
        size=len(get_close_matches(word, open_f.keys()))
        print("Suggests: ")
        for i in range(size):
            print("[%i]. "%(i+1) + get_close_matches(word, open_f.keys())[i])
        choose=int(input("Choose one number: "))
        choosen_word=get_close_matches(word, open_f.keys())[choose-1]
        print("%s :"%choosen_word)
        return(open_f[choosen_word])
    else:
        print("The word doesn`t exist")
word=input("To search: ")
output=Dictionary(word)
if type(output)==list:
    for item in output:
        print("*",item)
