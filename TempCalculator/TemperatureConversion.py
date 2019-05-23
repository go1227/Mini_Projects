__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "5/22/2019"
__python_version__ = "3"
__notes__ = "PEP8 compliant|command line execution"

import sys


def convert_f2c(temp):
    # Converts F to C, taking a float as the input parameter
    fahrenheit = float(temp)
    celsius = (fahrenheit - 32) * 5/9
    return celsius


def convert_c2f(temp):
    # Converts C to F, taking a flo at as the input parameter
    celsius = float(temp)
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


def main():
    if len(sys.argv) <= 1:
        print('Invalid input. Please enter F2C/C2F temp1 temp2 temp3 ... '.format(sys.argv[0]))
        sys.exit(0)

    operation = ''
    for arg in sys.argv[1:]:
        if operation == '':
            operation = arg
            operation = operation.upper()
        else:
            if operation in ['C2F', 'F2C']:
                try:
                    if operation == 'F2C':
                        result = convert_f2c(arg)
                    else:
                        result = convert_c2f(arg)
                except ValueError:
                    print("{!r} is not a numeric value".format(arg))
                else:
                    if operation == 'F2C':
                        print('{}\N{DEGREE SIGN}F : {}\N{DEGREE SIGN}C'.format(arg,round(result,2)))
                    else:
                        print('{}\N{DEGREE SIGN}C : {}\N{DEGREE SIGN}F'.format(arg, round(result,2)))
            else:
                print('\n\nFailed to load which calculator should be used!\n\n')
                break


if __name__ == '__main__':
    main()
