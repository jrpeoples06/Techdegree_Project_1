import random


def start_game():
    print("=================================================================")
    print("|  Welcome to the NUMBER GUESSING GAME created by Josh Peoples  |")
    print("=================================================================")
    try_again = True
    highscore = ''
    attempts = 1
    my_number = random.randint(1, 10)
    try:
        your_guess = int(input("\nPlease guess a number between 1 and 10: "))
    except ValueError:
        print("Oops..Thats not a number")
        your_guess = int(input("Please pick a number between 1 and 10: "))
    while try_again == True:
        try:
            if your_guess == my_number:
                if attempts == 1:
                    print("\nThat's the number! It took {} attempt.".format(attempts))
                else:
                    print("\nThat's the number! It took {} attempts.".format(attempts))
                    if highscore == '':
                        print("\nThat's a new HIGHSCORE!")
                        highscore = attempts
                    if attempts < highscore:
                        print("\nThat's a new HIGHSCORE!")
                        highscore = attempts
                    if attempts > highscore:
                        print("\nDang it..Not quite the highscore.")
                    play_again = input("\nWould you like to play again? (yes/no) ")
                    if play_again == 'yes':
                        my_number = random.randint(1, 10)
                        print("\nHIGHSCORE: {}".format(highscore))
                        your_guess = int(input("\nPlease guess a number between 1 and 10: "))
                        attempts = 1
                    if play_again == 'no':
                        print("Thanks for playing!")
                        try_again = False
                    elif play_again != 'no' and play_again != 'yes':
                        print("Oops..that is not a valid input. Please use either 'yes' or 'no' as a response.")
                        pass
            if your_guess < my_number:
                your_guess = int(input("It's higher: "))
                attempts += 1
            if your_guess > my_number:
                your_guess = int(input("It's lower: "))
                attempts += 1
        except ValueError:
            print("Oops..That's not a number.")
            pass


if __name__ == '__main__':
    start_game()
