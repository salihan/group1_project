import ast

dict1 = input("Enter first dictionary: ")
dict2 = input("Enter second dictionary: ")
merged_dict = ast.literal_eval(dict1) | ast.literal_eval(dict2)
print("Merged dictionary: ", merged_dict)
print("changes")

    