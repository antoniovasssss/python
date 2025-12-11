if True:
    print("true")

if False:
    print("false")


if False or False:
    print("no")

if True or False:
    print("yes")


num = 24

if num > 0:
    print("true")

if num % 2 == 0:
    print("false")


word = "bmw"

if word[0] == "d":
    print("yeah")
else:
    print("nah")


sentence = "roger that"

if sentence[-1] == "t":
    print("ends in a t")
else:
    print("does not end with t")

if len(sentence) <= 4:
    print("short")
else:
    print("long")