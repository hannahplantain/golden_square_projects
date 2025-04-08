## 1. Describe the Problem

# As a user
# So that I can improve my grammar
# I want to verify that a text starts with a capital letter 
# and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

    #name: improve_grammar

    #Parameters: one string

    #Returns: on string 

    #Side effects: returns "Give me a sentence to check, please." when an empty string is given


## EXAMPLES

#given an empty string, the function should return: "Give me a sentence to check, please."

#given "Hello world!" the function should return "Amazing Grammar!"

#given "how are you" the function should return "Grammar mistakes detected!"

def improve_grammar(string):
    punctuation = "!.?"
    if string == "":
        return "Give me a sentence to check, please."
    elif string[0].isupper() and string[-1] in punctuation:
        return "Amazing Grammar!"
    else: 
        return "Grammar mistakes detected!"