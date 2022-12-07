"""
COP 1500
This is a simple soccer quiz that will output your result at the end
"""
__author__ = "Joe Ramos"


def validate_answer(response, answer_list, message_wrong, message_right):
    """
This function serves to display a message to the user based on if their
response is right or wrong
    :param response: The input given by the user to the question
    :param answer_list: List of correct responses for the question.
    :param message_wrong:A message to tell the user their answer was incorrect
    :param message_right:A message to tell the user their answer was correct
    :return: True if the user entered a correct answer,else False
    """
    result = False
    for index in range(len(answer_list)):
        if response == answer_list[index]:
            result = True
            print(message_right)
            return result
        elif response != answer_list[index]:
            result = False
    if result is False:
        print(message_wrong)
    return result


def main():
    """
This is a function to run the core part of the code
    :return: True if the user attempts to start the program, else False
    """

    print("Hello User!")
    print("This quiz will test you on general soccer knowledge")
    start = input("Enter Y to start: ")
    while start not in ['y', 'Y']:
        start = input("Enter Y to start: ")
    start = start.strip()  # .strip() to remove spaces from the input
    print()  # This is just a space for the program to read better as it runs
    score = 0  # score starts at 0
    expert = False  # There is an expert question
    if start == "Y" or start == "y":
        # Question 1
        print("Question 1:", end=" ")
        print("What Jersey number does Cristiano Ronaldo currently wear?")
        print("(a)21")
        print("(b)7")
        print("(c)30")
        print("(d)8")
        question1_answer = input("Enter your answer choice: ")
        question1_answer = question1_answer.strip().lower()
        if question1_answer == "b" or question1_answer == "(b)" \
                or question1_answer == "7":
            print("Correct!")
            score += 1
        else:
            print("Wrong,Cristiano Ronaldo wears the jersey number 7.")
        print()

        # Question 2
        print("Question 2: " + "What nationality is Vinicius Jr.?")
        print("(a)Brazilian")
        print("(b)Portuguese")
        print("(c)American")
        print("(d)Canadian")
        question2_answer = input("Enter your answer choice: ")
        question2_answer = question2_answer.strip().lower()
        if question2_answer == "a" or question2_answer == "(a)" \
                or question2_answer == "brazilian":
            print("Correct!")
            score += 1
        else:
            print("Wrong, Vinicius Jr. is Brazilian.")
        print()

        # Question 3
        print("Question 3:", end=" ")
        print("Which nation won the last World Cup?")
        print("(a)Brazil")
        print("(b)Germany")
        print("(c)France")
        print("(d)Belgium")
        question3_answer = input("Enter your answer choice: ")
        question3_answer = question3_answer.strip().lower()
        if question3_answer == "c" or question3_answer == "(c)" \
                or question3_answer == "france":
            print("Correct!")
            score += 1
        else:
            print("Wrong, France won the last World Cup.")
        print()

        # Question 4
        print("Question 4:", end=" ")
        print("Who won the Ballon d'Or in 2021?")
        print("(a)Harry Kane")
        print("(b)Neymar Jr.")
        print("(c)Lionel Messi")
        print("(d)Robert Lewandoski")
        question4_answer = input("Enter your answer choice: ")
        question4_answer = question4_answer.strip().lower()
        if question4_answer == "c" or question4_answer == "(c)" \
                or question4_answer == "lionel messi":
            print("Correct!")
            score += 1
        else:
            print("Wrong, Lionel Messi won the last Ballon d'or.")
        print()

        # Question 5

        print("Expert Question:", end=" ")
        print("Which club won the 2022 Champions League Trophy?")
        print("(a)Liverpool")
        print("(b)Bayern Munich")
        print("(c)Chelsea")
        print("(d)Real Madrid")
        question5_answer = input("Enter your answer choice: ")
        question5_answer = question5_answer.strip().lower()
        wrong_message = 'Wrong,Real Madrid won the 2022 Champions League.'
        right_ans = ['d', '(d)', 'real madrid']
        if validate_answer(question5_answer, right_ans, wrong_message,
                           'Correct'):
            score += 1
            expert = True
        print()

    if score == 5 and expert:
        print("You are an expert! Your score was", str(score) + "/5")
    elif score >= 3:
        print("You passed, Your score was", str(score) + "/5")
    else:
        print("You failed, Your score was", str(score) + "/5")


# numeric operators
example_exponentiation = 5 ** 3  # ** this operator means to the power of __

example_multiplication = 5 * 3  # * this operator means multiplication

example_division = 5 / 3  # / this operator means division

example_modulus = 5 % 3  # % this operator means remainder of ___

example_floor_division = 5 // 3  # // this operator means to remove the decimal
#     and keep the integer after dividing

example_addition = 5 + 3  # + this operator means to add

example_subtraction = 5 - 3  # – this operator means to subtract

# string operators

example_string_repetition = ("hello" * 10)  # * repeats the string __ times
#   and concatenates them

example_concatenation = ("Hello" + " World")  # + puts the strings together

if __name__ == '__main__':
    main()
