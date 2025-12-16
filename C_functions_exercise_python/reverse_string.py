def reverse_string(text):
    # ensure the input is a string
    # this prevents issues if someone passes numbers or None
    text = str(text)
    # slice from end to start with a step of minus one
    # this builds a new string in reverse order
    return text[::-1]

print(reverse_string("hello"))   # olleh
print(reverse_string("Python"))  # nohtyP