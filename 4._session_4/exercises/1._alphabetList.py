# 1. Create a list of capital letters in the english alphabet
result = [ chr(i) for i in range(65, 91) ]

print(result)

# 2. Create a list of capital letter from the english aplhabet, but exclude 4 with the Unicode code point of either 70, 75, 80, 85.
result_2 = [ chr(i) for i in range(65, 91) if i not in [70, 75, 80, 85] ]

print(result_2)

# 3. Create a list of capital letter from from the english aplhabet, but exclude every second between F & O
result_3 = [ chr(i) for i in range(65, 91) if i not in range(70, 80, 2)]

print(result_3)