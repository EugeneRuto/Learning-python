# # numbers
# num1=10
# num2=10.5
# first_name="Nuru"

# cars=["Mercedes", "Subaru", "Toyota"]
# names=("Eugene", "Ruto", "Maxwell")
# str="printing double quotes"
# bloodtypes=["A", "B" , "O" ,"AB"]

# print(type(num1))
# print(type(num2))
# print(type(first_name))
# print(type(cars))
# print(type(names))
# print(str)
# print(type(str))
# print(bloodtypes)
# print(type(bloodtypes))

# # immutability of integers

# x=10
# print(id(x))  # ID of `x` before modification

# x=20
# print(id(x)) #after modification

# x = x + 5
# print(x)       # Output: 15
# print(id(x))   # ID of `x` after modification

# checking if lists are mutable

# my_list=[1,2,3,4]
# print(id(my_list), "The original list", my_list)   #the original list

# my_list[0]=20     #adding 20 at indice 0
# my_list.append(5) #adding 5 at the end of the list
# print(id(my_list), "The modified list", my_list)    #after modification

# checking if tuple is immutable
# Create a tuple
# my_tuple = (1, 2, 3)
# print("Original tuple:", my_tuple)

# # Try modifying the tuple
# try:
#     my_tuple[0] = 10  # This will raise an error
# except TypeError as e:
#     print("Error:", e)

# # immutability of strings
# original_string = "hello"
# print("Original String ID:", id(original_string))

# # Attempt to change the first character
# modified_string = original_string.replace("h", "y")  # Creates a new string
# print("Modified String:", modified_string)
# print("Modified String ID:", id(modified_string))

# # Original string remains unchanged
# print("Original String:", original_string)


#string concatenation

insult_1="we"
comma=" "
insult_2="mjinga"
complete_insult=insult_1+comma+insult_2
print(complete_insult)










