# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x >= 8:
        print("X больше либо равен 8")
        y = ((a * a) + 4*(x*x) + b) / a*b
    else:
        print("X меньше 8")
        y = (a * a) - 2*(x*x)
    print("y = %.2f" % y)


if __name__ == '__main__':
    main()
