def find_char_positions(s: str, ch: str) -> None:
    # ensure the target is a single character so the intent is clear
    if len(ch) != 1:
        # early return if the input is not a single character
        return
    # loop over the string while keeping the index with enumerate
    for i, c in enumerate(s):
        # check if the current character equals the target character
        if c == ch:
            # print the index when we find a match
            print(i)
            
find_char_positions("banana", "a")