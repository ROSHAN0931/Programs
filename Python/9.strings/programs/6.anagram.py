#  Create a program that checks if two given strings are anagrams of each other.

a=input("Enter string : ")
b=input("Enter string : ")
sa=sorted(a.lower())
sb=sorted(b.lower())
# print(sa)
# print(sb)

if sa==sb:
    print("anagram")
else:
    print("not anagram")