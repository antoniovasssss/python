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