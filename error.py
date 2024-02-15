def calc_square_root(n):

    try:
        from my_calculator import sqrt
    except ModuleNotFoundError:
        from math import sqrt

    if n < 0:
        raise ValueError("Cannot use a negative number with sqrt")
    answer = sqrt(n)
    return answer


def main():
    try:
        print(calc_square_root(-2))
    except ModuleNotFoundError:
        print("The module my_calculator was not found.  Copy to folder.")
    except ValueError:
        print("You cannot use a negative number.")
    print("End")


if __name__ == "__main__":
    main()
