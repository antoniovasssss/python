def keep_it_quiet(text):
    lowered = text.lower()
    result = lowered + "..."
    return result

if __name__ == "__main__":
    print(keep_it_quiet("HOORAY"))
    print(keep_it_quiet("Doggo"))
    print(keep_it_quiet("What?!"))