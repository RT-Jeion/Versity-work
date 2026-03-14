# Implement a function that checks if a given string is an anagram of another string using a dictionary.

def anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if len(s1) != len(s2):
        return False

    s1_dict = {}
    s2_dict = {}
    
    for i in range(len(s1)):
        if s1[i] in s1_dict.keys():
            s1_dict[i] += 1

        else:
            s1_dict[i] = 1
        
        if s2[i] in s2_dict.keys():
            s2_dict[i] += 1

        else:
            s2_dict[i] = 1

    if s1_dict == s2_dict:
        return True

text1 = input("Enter the 1st Text: ")
text2 = input("Enter the 2nd Text: ")

result = anagram(text1, text2)

if result:
    print(f"{text1} and {text2} are Anagram")
else:
    print(f"{text1} and {text2} are not Anagram")
