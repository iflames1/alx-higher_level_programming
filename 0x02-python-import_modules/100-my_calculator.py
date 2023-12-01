#!/usr/bin/python3

if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if argv[2] == '+':
        result = calc.add(int(argv[1]), int(argv[3]))
    elif argv[2] == '-':
        result = calc.sub(int(argv[1]), int(argv[3]))
    elif argv[2] == '*':
        result = calc.mul(int(argv[1]), int(argv[3]))
    elif argv[2] == '/':
        result = calc.div(int(argv[1]), int(argv[3]))

    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
