def keep_it_quiet(text): # function takes a string
    lowered = text.lower() # converts the string to lowercase
    result = lowered + "..." # then after its converted it appends the "..." 
    return result

if __name__ == "__main__":
    print(keep_it_quiet("HOORAY"))
    print(keep_it_quiet("Doggo"))
    print(keep_it_quiet("What?!"))