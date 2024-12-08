import random
letters =["A","B", "C", "D", "E", "F", "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S","T", "U", "V", "W", "X", "Y", "Z","a", "b", "c", "d", "e", "f", "g", "h", "i","j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7","8","9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-","_","+","="]
Pw_letters = int(input("Enter number of letters: "))
Pw_numbers = int(input("Enter number of numbers: "))
Pw_symbols = int(input("Enter number of symbols: "))
Password = []
for i in range (0,Pw_letters):
  Password.append(random.choice(letters))
for i in range (0,Pw_numbers):
  Password.append(random.choice(numbers))
for i in range (0,Pw_symbols):
  Password.append(random.choice(symbols))

print(Password)
random.shuffle(Password)
for i in range(0,len(Password)):
  print(Password[i],end="")