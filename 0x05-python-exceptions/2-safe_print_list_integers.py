def safe_print_list_integers(my_list=[], x=0):

    moon = 0

    for i in range(x):

        try:

            print("{:d}".format(my_list[i]), end="")
            moon += 1

        except (TypeError, ValueError):
            pass

    print()

    return (moon)
