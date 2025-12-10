#Beginner - List Comprehension
# 1) List of numbers from 1 to 20
nums_1_to_20 = [n for n in range(1, 21)]        # iterate n from 1 up to 20 inclusive and collect n
print(nums_1_to_20)                              # show the result
# Reason because range(1, 21) produces 1 through 20 and the comprehension collects each n


# 2) List of squares for numbers 1 to 10
squares_1_to_10 = [n * n for n in range(1, 11)] # iterate n from 1 to 10 and compute n times n
print(squares_1_to_10)                           # show the result
# Reason because we transform each n into its square during collection


# 3) List of even numbers from 1 to 50
evens_1_to_50 = [n for n in range(1, 51) if n % 2 == 0]  # iterate n then keep it only if divisible by 2
print(evens_1_to_50)                                     # show the result
# Reason because the if filter keeps only values whose remainder modulo 2 is zero


# 4) Convert all names in a list to uppercase
names = ["alice", "Bob", "carol"]            # sample input list of names
upper_names = [name.upper() for name in names]  # iterate name then call .upper on each and collect it
print(upper_names)                              # show the result
# Reason because str.upper returns a new uppercase string for each element


# 5) Extract only vowels from a given string
text = "List Comprehension Practice"                 # sample input string
vowels = "aeiouAEIOU"                                # characters we consider vowels
only_vowels = [ch for ch in text if ch in vowels]    # iterate ch then keep it only if it is in vowels
print(only_vowels)                                   # show the result as a list of characters
print("".join(only_vowels))                          # optional join to make a single string of vowels
# Reason because the membership test ch in vowels filters to vowel characters only


#Intermediate 
# 1) Numbers between 1 and 100 divisible by both 3 and 5
div_by_3_and_5 = [n for n in range(1, 101) if n % 3 == 0 and n % 5 == 0]
print(div_by_3_and_5) # [15, 30, 45, 60, 75, 90]
# n comes from 1 to 100
# keep n only if n mod 3 equals 0 and n mod 5 equals 0

# 2) Keep only positive numbers
nums = [1, -2, 3, -4, 5]
positives = [n for n in nums if n > 0]
print(positives) # [1, 3, 5]
# take each n from nums
# keep it only if n greater than 0

# 3) Words longer than 4 characters
sentence = "List comprehension practice can be very fun"
long_words = [w for w in sentence.split() if len(w) > 4]
print(long_words)  # ['comprehension', 'practice']
# split the sentence into words
# keep a word only if its length is greater than 4

# 4) Strings that start with the letter a
words = ["apple", "Banana", "avocado", "cherry", "Apricot"]
a_words = [w for w in words if w.lower().startswith("a")]
print(a_words)  # ['apple', 'avocado', 'Apricot']
# take each word
# make it lowercase for case insensitivity
# keep it only if it starts with a

# 5) Tuples of (number, square_of_number) for 1 to 10
pairs = [(n, n*n) for n in range(1, 11)]
print(pairs) # [(1, 1), (2, 4), ..., (10, 100)]
# n goes from 1 to 10
# build a tuple with n and n squared


#advanced 
matrix = [[1, 2], [3, 4], [5, 6]] # a list of lists
flat = [x for row in matrix for x in row] # for each row then for each item x in that row
print(flat) # [1, 2, 3, 4, 5, 6]

# build numbers from 2 to 100 since 1 is not prime
primes = [
    n for n in range(2, 101)
    if all(n % d != 0 for d in range(2, int(n**0.5)+1))
]
print(primes)

words = ["apple", "Banana", "avocado", "apricot"]
reversed_words = [s[::-1] for s in words]
print(reversed_words)


#Dictionary Comprehension
#beginner
cubes = {n: n**3 for n in range(1, 6)}
print(cubes)

names = ["ram", "shyam", "hari"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)

keys = [1, 2, 3] #given keys
values = ["a", "b", "c"] #given values
paired = {k: v for k, v in zip(keys, values)} #pair and build dict
print(paired) #{1: 'a', 2: 'b', 3: 'c'}

#intermediate 
d = {"a": 1, "b": 2, "c": 3} # sample input dictionary
flipped = {v: k for k, v in d.items()} # build a new dict where each value becomes the key and each key becomes the value
print(flipped) # show the result

evens_sq = {n: n**2 for n in range(1, 21) if n % 2 == 0} # pick numbers 1..20 then keep only evens then map to square
print(evens_sq) # show the result

scores = {"x": 5, "y": 12, "z": 30, "w": 9}
filtered = {k: v for k, v in scores.items() if v > 10}
print(filtered)

#advanced 
s = "banana banana"
chars = set(s)
freq = {c: s.count(c) # map each char to how many times it appears
        for c in chars
        if c != " "}  # loop unique characters
print(freq)

sentence = "Fries and chicken strips for life"
words = sentence.split() # break into words by spaces
lenghts = {w: len(w)
           for w in words}# loop all words
print(lenghts)

text = "Abracadabra forever"
vowels = "aeiou"
t = text.lower()
vowels_counts = {v: t.count(v)
                 for v in vowels
                 if t.count(v) > 0}
print(vowels_counts)



#set comprehension
#beginner
squares = {n * n for n in range(1, 11)} # n goes from 1 to 10 and we add n*n to the set
print(squares) # show the resulting set of squares

nums = [1, 2, 3, 3, 3, 4, 5, 5]  # list containing repeated numbers
unique_vals = {x for x in nums} # add each element x from the list into a set
print(unique_vals)

text = "Comprehension practice in Python" 

vowels = {"a", "e", "i", "o", "u"} # define the vowel set in lowercase

unique_vowels = {ch.lower() # take the lowercase version of the character
                 for ch in text # loop through each character in the string
                 if ch.lower() in vowels}  # keep it only if it is a vowel
print(unique_vowels) # show the unique vowels found

div_by_7 = {n  # keep the current number
            for n in range(1, 101) # iterate from 1 through 100
            if n % 7 == 0} # include it only if divisible by 7
print(div_by_7) # show the set of numbers divisible by 7

#advanced
sentence = "Comprehension practice in Python" # your input sentence
first_letters = {word[0].lower() # take the first character then normalize case
                 for word in sentence.split()# split the sentence into words by whitespace
                 if word} # guard against empty strings
print(first_letters) # show the unique first letters

#Create a dictionary to count vowel occurrences in a string.
text = "Set 123 comprehension 256!"  # your input text

no_digits_chars = {ch # keep the character as is
                   for ch in text # iterate through each character
                   if not ch.isdigit()} # exclude characters that are digits
print(no_digits_chars) # show unique characters without digits



#generator expression
#beginner
# create a generator that yields squares from 1 to 10
squares = (n * n for n in range(1, 11))  # n runs from 1 to 10. each yield is n squared

# consume the generator and show the results
for value in squares: # iterate through each produced square
    print(value) # print the current square

#Create a generator that yields even numbers from 1–50.
evens = (n for n in range(1, 51) if n % 2 == 0) # n runs 1 to 50. keep n only if n mod 2 equals zero

for value in evens: # iterate through each even number
    print(value) # print the current even number

#intermediate
#Create a generator for Fibonacci numbers (first 10 values)
def fib (n):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a, b, = b, a + b

first_ten = fib(10)
for value in first_ten:
    print(value)

#Generator that yields characters of a string one-by-one
text = "Hello world"

chars = (ch for ch in text) # generator expression that produces each character

for ch in chars: # iterate through each produced character
    print(ch) # print the current character

#advanced
#Create a generator that produces infinite multiples of 5
def multiples_of_5():
    n = 1 # start at the first multiple index
    while True: # loop forever to make an infinite stream
        yield 5 * n # produce the current multiple
        n += 1 # move to the next index

from itertools import islice # tool to slice an iterator
first_ten = list(islice(multiples_of_5(), 10)) # pull ten values lazily
print(first_ten) # prints [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

#Create a generator that reads a file line by line
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f: # the file yields one line at a time
            yield line.rstrip("\n") # strip the newline and yield lazily

for line in read_lines("data.txt"): # replace with your file path

    print(line)