import json
from difflib import get_close_matches


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean " + get_close_matches(word, data.keys())[0])
        decision = input("press y or n ")
        if decision == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decision == "n":
            return "Please Enter properly"
        else:
            return "Wrong input"
    else:
        return "Word does not exitst"


data = json.load(open("data.json"))
while True:
    word = input("Enter the word you want to search (0 to exit) ")
    if word == "0":
        break
    output = translate(word)

    if type(output) == list:
        for idx, item in enumerate(output):
            print(str(idx + 1) + ".", item)
    else:
        print(output)
    print("\n")
