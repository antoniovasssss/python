nonsense = "this is just a sentence" # create the string and store it in nonsense

has_st = "st" in nonsense #true if "st" appears in the string

if has_st: #if the substring is present
    print("yeet")
elif len(nonsense) > 10:
    print("yo")
else:
    print("no")

has_zoo = "zoo" in nonsense
has_fun = "fun" in nonsense

if has_zoo and has_st: #both present
    print("cool")
elif has_st: #only "st" pressent
    print("rad")
elif has_fun: #only "fun" present
    print("dope")
else: #none present
    print("nope")



q = 24
if q % 3 == 0 and q % 5 == 0:
    print("both")
elif q % 3 == 0 or q % 5 == 0:
    print("either")
else:
    print("neither")

r = 9
if r % 3 == 0 and r % 5 == 0:
    print("both")
elif r % 3 == 0 or r % 5 == 0:
    print("either")
else:
    print("neither")

s = 15
if s % 3 == 0 and s % 5 == 0:
    print("both")
elif s % 3 == 0 or s % 5 == 0:
    print("either")
else:
    print("neiher")