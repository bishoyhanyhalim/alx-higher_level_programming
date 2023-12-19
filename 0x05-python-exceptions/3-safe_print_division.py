def safe_print_division(a, b):

    try:
        book = (a / b)

    except ZeroDivisionError:
        book = None

    finally:
        print("Inside book: ", end="")

        print("{}".format(book))

    return (book)
