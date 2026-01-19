colors = ["red", "purple", "orange"]


for color_str in colors: # the outer loop goes through each color name, then prints the string i.e red
    print(color_str)
    for char in color_str: # the inner loop breaks that color name into individual letters i.e r e d
        print(char)
    print()
