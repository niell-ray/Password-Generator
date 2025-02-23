import random as rand
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# list to store the password elements.
random_password_lst = []

# loop to generate desired no of letters in random.
for i in range(0, nr_letters):
    random_password_lst.append(rand.choice(letters))

# loop to generate desired no of symbols in random.
for k in range(0, nr_symbols):
    random_password_lst.append(rand.choice(symbols))

# loop to generate desired no of numbers in random.
for j in range(0, nr_numbers):
    random_password_lst.append(rand.choice(numbers))

# printing the list.
print(random_password_lst)

# shuffling each element and then printing the list.
rand.shuffle(random_password_lst)
print(random_password_lst)

# printing the password as string.
password = ""
for item in random_password_lst:
    password += item
print(f"Your new password: {password}")
