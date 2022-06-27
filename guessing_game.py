"""This is a simple guessing game. You get 5 tries to guess the password."""
password = "spicejet"
guess_limit = 5
choice = 'Y'
while choice == 'Y': 
    guess_word = ""
    guess_count = 0

    print("Welcome to the GUESSING GAME. You have 5 guesses to get the right password..")

    while (guess_word != password) and (guess_count != guess_limit):
        guess_word = input("Enter your guess: ")
        guess_count += 1

    if guess_word != password:
        print("Sorry...You are out of guess...")
        choice = input("Do you want to play again?(Y/N) ")
    else:
        print("You guessed the password correctly. You WIN!")
        choice = 'N'

