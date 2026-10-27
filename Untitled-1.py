#input word

text = str(input("enter a string: "))

# reverse string
# using step value as -1 to lterate in reverse
revtext = text[::-1]
text =revtext

print(" reversed of given string:")
print(text)