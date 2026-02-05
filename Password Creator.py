from random import randint

# User inputs the password
u_pwd = input("Enter your desired Character: ")

# List of possible characters in the password (A-Z, a-z, 0-9)
pwd = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Initialize an empty string for the guessed password
pw = ""

# Loop until the guessed password matches the user's password
while pw != u_pwd:
    pw = ""
    for _ in range(len(u_pwd)):
        # Randomly select a character from the list to guess
        guess_pwd = pwd[randint(0, len(pwd) - 1)]
        pw += guess_pwd
    
    # Print the guessed password in each iteration
    print("Creaking Password :","\033[32m",pw,"\033[0m")

# Once the loop exits, the password has been cracked
print("Password cracked:","\033[33m", pw,"\033[0m")
