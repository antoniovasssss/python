def no_ohs(text: str) -> None:  # define a function that takes a string and returns nothing
    for ch in text: # iterate one character at a time
        if ch == 'o': # check if the character is the lowercase letter o
            continue # skip printing this character
        print(ch) # print allowed characters on their own line
        
no_ohs("code")
no_ohs("book")
no_ohs("hello")