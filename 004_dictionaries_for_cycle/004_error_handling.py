# Try - Except statement

# Get user input
code = input('Please enter your id: ')

try:
    int(code)  # Check if the input can be converted to an integer
    if len(code) != 11:
        raise UserWarning('The length of your code is not equal to 11')
except ValueError:
    print('Your code should contain only numbers!')
except UserWarning:
    print('Your code should consist of exactly 11 digits!')
else:
    print(f'Your code {code} was checked successfully!')
finally:
    del code  # Cleanup