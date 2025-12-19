def string_iterate(text):
     # define a function named string_iterate that takes one parameter called text

    for ch in text:
    # start a loop that visits each character in the string text in order

        print(ch)
         # print the current character on its own line

if __name__ == "__main__":
    # run the examples only when this file is executed directly

    string_iterate("celery") # prints c e l e r y one per line
    string_iterate("hat") # prints h a t one per line