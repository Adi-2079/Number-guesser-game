import random

def number_guesser_game():
    print("Hello! This is a number guesser game! To play this game type P. To end the game press N")
    letter = input().strip().upper()  # Use .strip() to remove any leading/trailing whitespace and .upper() to handle lowercase inputs

    if letter == "P":
        print("Great, let's begin the game!")
        print("I am thinking of a number from 1 - 300. You have infinite questions to guess the number")
        print("The questions you can ask are, 'is it higher than ___', 'is it odd', 'is it even', 'is it lower than ___'. If at any time you want to make your final guess, type F. Note that you can make only one final guess.")

        random_number = random.randint(1, 300)
        questions_asked = 0

        while True:
            print("Guess a number or ask a question:")
            question = input().strip()

            if question.isdigit():
                guess = int(question)
                questions_asked += 1
                if guess != random_number:
                    print("Sorry, wrong number")
                    if guess > random_number:
                        print("The number is less")
                    elif guess < random_number:
                        print("The number is higher")
                else:
                    print("You guessed the number!")
                    print(f"It took you {questions_asked} questions to guess the number")
                    break
            elif question.upper() == "F":
                final_guess = int(input("Enter your final guess: ").strip())
                questions_asked += 1
                if final_guess == random_number:
                    print("Congratulations! You guessed the number correctly!")
                else:
                    print(f"Sorry, the correct number was {random_number}.")
                print(f"It took you {questions_asked} questions.")
                break
            else:
                if question.lower().startswith("is it higher than"):
                    num = int(question.split()[-1])
                    print("Yes" if random_number > num else "No")
                elif question.lower().startswith("is it lower than"):
                    num = int(question.split()[-1])
                    print("Yes" if random_number < num else "No")
                elif question.lower() == "is it odd":
                    print("Yes" if random_number % 2 != 0 else "No")
                elif question.lower() == "is it even":
                    print("Yes" if random_number % 2 == 0 else "No")
                else:
                    print("Invalid question, please try again.")
                questions_asked += 1
    else:
        print("Goodbye!")

number_guesser_game()
