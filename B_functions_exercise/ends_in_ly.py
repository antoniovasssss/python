def ends_in_ly(s: str) -> bool:
    #Return True if the string ends with 'ly'
    #Otherwise return False
    # s.endswith('ly') checks the last two characters of s
    #It returns True when s ends with 'ly' and False otherwise
    return s.endswith('ly')

if __name__ == '__main__':
    # Sample checks from the prompt
    print(ends_in_ly("pretty"))     # False
    print(ends_in_ly("instant"))    # False
    print(ends_in_ly("analytic"))   # False
    print(ends_in_ly("timidly"))    # True
    print(ends_in_ly("fly"))        # True
    print(ends_in_ly("gallantly"))  # True