#odd or even
num = 17

if num % 2 == 0:
    print("even")
else:
    print("odd")


#password strength
password = "Pass123"

if len(password) < 4:
    print("too short")
elif password.isalpha():
    print("weak")
elif password.isalnum():
    print("medium")
else:
    print("strong")



#temperature detector
temp = 32

if temp < 0:
    print("freezing")
elif temp < 20:
    print("cold")
elif temp < 30:
    print("warm")
else:
    print("hot")



#vowel or cosonant
ch = "e"

if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")



#age group classifier
age = 15

if age < 13:
    print("child")
elif age < 20:
    print("teen")
elif age < 60:
    print("adult")
else:
    print("elder")