import sys


def calculate_factorial(cursor, consider):
    if cursor > 1:
        consider *= cursor
        cursor -= 1
        calculate_factorial(cursor, consider)
    else:
        print(consider)


def main():
    print("Factorial")
    calculate_factorial(5, 1)


if __name__ == '__main__':
    sys.exit(main())
