# Write a program that finds the most frequent word in a given text (use a dictionary).

text = input("Enter your String: ")
text = text.lower()
freq_dict = {}

for i in text:
    if i in freq_dict.keys():
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

count = 0
result = []
for i in freq_dict:
        
    if freq_dict[i] > count:
        count = freq_dict[i]
        result = [i]
        
    elif freq_dict[i] == count:
        result.append(i)

print("Entered text:", text)
print("Most frequent word:", end=" ")
for i in result:
    print(i, end=" ")
print("\nCount:", count)
