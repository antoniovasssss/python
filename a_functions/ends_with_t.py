def ends_with_t(text):
    return text[-1] == "t" # the expression text[-1] accesses the last character of the string.
    # then == "t" checks if that character is equal to "t", returning True or False
    

print(ends_with_t("smart"))     
print(ends_with_t("racket"))     
print(ends_with_t("taco"))       
print(ends_with_t("boomerang"))