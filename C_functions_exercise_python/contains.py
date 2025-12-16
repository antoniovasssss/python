def contains(str1, str2):
    # Convert the first string to lowercase so case is ignored
    s1 = str(str1).lower()
    # Convert the second string to lowercase so case is ignored
    s2 = str(str2).lower()
    # Check if s2 appears anywhere inside s1 and return that boolean
    return s2 in s1

# Simple checks that match the prompt examples
print(contains("caterpillar", "pill"))      # True because "pill" occurs in "caterpillar"
print(contains("lion's share", "on"))       # True because "on" occurs in "lion's share"
print(contains("SORRY", "or"))              # True because "or" occurs after lowercasing "SORRY"
print(contains("tangent", "gem"))           # False because "gem" is not in "tangent"
print(contains("clock", "ok"))              # False because "ok" is not in "clock"