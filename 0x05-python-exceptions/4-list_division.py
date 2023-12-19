def list_division(my_list_1, my_list_2, list_length):
    hi_book = []

    for i in range(0, list_length):
        try:
            hello = my_list_1[i] / my_list_2[i]

        except TypeError:
            print("wrong type")
            hello = 0

        except ZeroDivisionError:
            print("division by 0")
            hello = 0

        except IndexError:
            print("out of range")
            hello = 0

        finally:
            hi_book.append(hello)

    return (hi_book)
