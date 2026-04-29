
def remove_duplicate(user_input):
    temp_set = set()
    deduplicate = []

    for input in user_input:
        if input not in temp_set:
            temp_set.add(input)
            deduplicate.append(input)

    return deduplicate

user_input = input("Enter the number seperated by spaces.")

try :
    numbers = [int(x) for x in user_input.split()]
    uniquelist = remove_duplicate(numbers)
    print(f"List without duplicates: {uniquelist}")
except ValueError: 
    print("Please enter valid integer seperated by spaces")

#-------------------- 2 ----------------------
sentence = input("Enter a sentence: ")
words = sentence.split()

word_frequency = {}  
# Count frequency of each word
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

print(word_frequency)
print("\nDisplay in a proper way as requested in example output..")
for word, count in word_frequency.items():
    print(f"{word}: {count}")

#-------------------- 3 ----------------------
import ast

dict1 = input("Enter first dictionary: ")
dict2 = input("Enter second dictionary: ")
merged_dict = ast.literal_eval(dict1) | ast.literal_eval(dict2)
print("Merged dictionary: ", merged_dict)