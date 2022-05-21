#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
list_of_letters = []
list_of_symbols = []
list_of_numbers = []
len_letters = len(letters) - 1
len_symbols = len(symbols) - 1
len_numbers = len(numbers) - 1


##FOR LETTERS##
for num_letter in range(0, (nr_letters)):
  #No need to change the 'random_num' variable name, change ONLY the 'len(*change this*)''#
  random_num = random.randint(0, len_letters)
  
  letters_chosen = [letters[random_num]]
  list_of_letters.extend(letters_chosen)
  # print(letters_chosen)
# print(list_of_letters)



##FOR SYMBOLS##
for num_symbol in range(0, (nr_symbols)):
  #No need to change the 'random_num' variable name, change ONLY the 'len(*change this*)''#
  random_num = random.randint(0, len_symbols)
  
  symbols_chosen = [symbols[random_num]]
  list_of_symbols.extend(symbols_chosen)
  # print(symbols_chosen)
# print(list_of_symbols)



##FOR NUMBERS##
for num_number in range(0, (nr_numbers)):
  #No need to change the 'random_num' variable name, change ONLY the 'len(*change this*)''#
  random_num = random.randint(0, len_numbers)
  
  numbers_chosen = [numbers[random_num]]
  list_of_numbers.extend(numbers_chosen)
  # print(numbers_chosen)
# print(list_of_numbers)

# password

password = ("")
all_combined = []

all_combined.extend(list_of_letters + list_of_symbols + list_of_numbers)
# print(all_combined)

###PASSWORD GENERATED IN ORDER###
# for i in all_combined:
#   password += str(i)
# print(f"Your password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
random.shuffle(all_combined)
for i in all_combined:
  password += str(i)
print(f"Your password is: {password}")