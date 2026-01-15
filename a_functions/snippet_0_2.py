def how_many():
    return 42
# this prints the function object itself, not the result of calling it
print(how_many)
# the parenthesis () call the function, which returns 42, so this prints 42
print(how_many())
# since the_answer was assigned the return value of how_many(), this also prints 42
the_answer = how_many()
print(the_answer)

def how_many():
    5 # does nothing

print(how_many())