__author__ = "Gil Ortiz"
__version__ = "1.1"
__date_last_modification__ = "5/28/2019"
__python_version__ = "3"
__notes__ = "PEP8 compliant | command line execution"

import sys

def convert_f2c(temp):
    # Converts F to C, taking a float as the input parameter
    celsius = (float(temp) - 32) * 5/9
    return celsius

def convert_c2f(temp):
    # Converts C to F, taking a float as the input parameter
    fahrenheit = float(temp) * 9/5 + 32
    return fahrenheit

def main():
    if len(sys.argv) <= 1:
        print("Invalid input. Please enter F2C/C2F temp1 temp2 temp3 ... ")
        sys.exit(0)

    operation = ''
    for arg in sys.argv[1:]:
        if operation == '':
            operation = arg.upper()
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
                    if operation == 'C2F':
                        print(f"{arg}\N{DEGREE SIGN}C : {str(round(result,2))}\N{DEGREE SIGN}F")
                    else:
                        print(f"{arg}\N{DEGREE SIGN}F : {str(round(result, 2))}\N{DEGREE SIGN}C")
            else:
                print('\n\nFailed to load which calculator should be used!\n\n')
                break

if __name__ == '__main__':
    main()
