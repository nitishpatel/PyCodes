from random import *
characters = "0123456789" #ALL THE NUMBERS
password = "".join(choice(characters) for x in range(6)) #Generates otp of size 6 
print(password)
