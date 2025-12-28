def remove_capitals(text):
    # build a new string with only non-uppercase characters
    result = ""
    for char in text:
        if not char.isupper():
            result += char
    return result

print(remove_capitals("fOrEver"))
print(remove_capitals("raiNCoat")) 
print(remove_capitals("cElLAr Door"))
