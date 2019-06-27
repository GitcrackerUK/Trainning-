

#1
def vowelcheck(letter):
    vowel="aeiou"
    if letter in vowel:
        print("letter is vowel")
    else:
        print("Letter is consonant")


vowelcheck("a")
vowelcheck("c")
vowelcheck("d")
vowelcheck("z")
vowelcheck("u")


#2
def vowelcheck2(letter):
    vowel="aeiou"
    return letter in vowel
print(vowelcheck2("a"))
print(vowelcheck2("e"))
print(vowelcheck2("i"))
print(vowelcheck2("o"))
print(vowelcheck2("u"))