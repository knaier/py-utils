while True:
    first_number = input('First Number: ')
    second_number = input('Second Number: ')

    if first_number == 'q' or second_number == 'q':
        break

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by 0!")
    except FileNotFoundError:
        # Pass is if you want to ignore the error, no stack will be thrown at this point
        pass
    else:
        # You shouldnt do this in the try, it should be only the code that could trigger the exception. This is why the try-catch-else block is important
        print(f"The answer is {answer}")