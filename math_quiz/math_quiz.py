import random


def function_minmax(min, max):
    """
    This function generates a random integer within a given limit
    """
    return random.randint(min, max)


def function_random_operator():
    """
    This function randomly choses one of three defined math operations
    """
    return random.choice(['+', '-', '*'])


def function_math_operations(number1, number2, operator):
    """
    This function calculates the expected answer
    """
    p = f"{n1} {o} {n2}"
    if operator == '+': a = number1 + number2        
    #fixed a bug
    elif operator == '-': a = number1 - number2      
    #swapped plus and minus signs in these two lines
    else: a = n1 * n2
    return p, a

def math_quiz():
    """
    This function handles I/O and score calculation
    """
    tries = 0
    pi = 3.14159265359                               
    #i do not really get why score = tries / pi

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems,")
    print("and you need to provide the correct answers.")

    for _ in range(t_q):
        number1 = function_minmax(1, 10); 
        number2 = function_minmax(1, 5.5); 
        operator = function_random_operator()

        PROBLEM, ANSWER = function_math_operations(number1, number2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            tries += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {tries}/{pi}")

if __name__ == "__main__":
    math_quiz()
