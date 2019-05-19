__author__ = "Gil Ortiz"
__version__ = "1.0"
__date_last_modification__ = "5/18/2019"
__python_version__ = "3"
__notes__ = "PEP8 compliant|on-screen results"

# 3 inputs are required: SPHERE, CYLINDER, AXIS
user_input = []


def astigmatism_conversion(user_entry):  # Function responsible for the Astigmatism Conversions
    a = user_input[0]
    b = user_input[1]
    c = user_input[2]

    # Sphere result
    aux = str(float(a) + float(b))
    if len(aux.split('.')[1]) == 1:
        aux = aux + '0'
    if '-' in aux:
        pass
    else:
        aux = '+' + aux
    result = [aux]

    # Cylinder result
    aux = b
    if '-' in aux:
        aux = aux.replace('-', '+')
    result.append(aux)

    # Axis result
    aux = int(c)
    if aux + 90 > 180:
        aux -= 90
    else:
        aux += 90
    result.append(aux)
    print("\n\n")
    print(f' INPUT = {user_entry[0]} {user_entry[1]} x {user_entry[2]}')
    print(f'OUTPUT = {result[0]} {result[1]} x {result[2]}')


basic_numbers = list(range(0, 10))
available_decimals = ['00', '25', '50', '75']

good_values = []  # list containing all possible acceptable SPHERE and CYLINDER values
for n in basic_numbers:
    for m in available_decimals:
        tmp = str(n) + '.' + m
        good_values.append('+'+tmp)
        good_values.append('-'+tmp)

# Input 1: SPHERE value
valid_entry = False
while valid_entry is False:
    sphere = input("\n\n-------------------------\nEnter the SPHERE value:")
    sphere = sphere.replace(' ', '').strip()
    if sphere in good_values:
        valid_entry = True
        user_input.append(sphere)
    else:
        print("\nSphere must be a decimal and multiple of .25 and must contain + or - symbol")

# Input 2: CYLINDER value
valid_entry = False
while valid_entry is False:
    cylinder = input("\n\n-------------------------\nEnter the CYLINDER value:")
    cylinder = cylinder.replace(' ', '').strip()
    if cylinder in good_values:
        valid_entry = True
        user_input.append(cylinder)
    else:
        print("\nCylinder must be a decimal and multiple of .25 and must contain + or - symbol")

# Input 1: AXIS value
valid_entry = False
while valid_entry is False:
    axis = input("\n\n-------------------------\nEnter the AXIS value:")
    axis = axis.replace(' ', '').strip()
    if axis.isnumeric():
        valid_entry = True
        user_input.append(axis)
    else:
        print("\nAxis must be an integer (0 - 180)")


# call main function that will convert the input data and print out the results
astigmatism_conversion(user_input)
