# Write a program that:
#
# 1. Finds age using provided years (current_year, year_of_birth)
# 2. Find missing code part (code_2):
#    - find a remainder of x divided by y
#    - multiply the result by 13
#    - find a square root of result (same as power of 0.5)
#    - leave only whole part of result
# 3. Save code to a separate variable
# example:
# 475-12-967
# 4. Print line using data from variables:
# example:
# Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.


# years
current_year = 2023
year_of_birth = 1988

# code parts
code_1 = '354'
code_3 = 132

# name
user_name = 'John'
user_surname = 'Smith'

# code 2 data
x = 152
y = 132

age = current_year - year_of_birth

code_2 = str(int((x % y * 13) ** 0.5))  # 20
code = code_1 + '-' + code_2 + '-' + str(code_3)

print("Hello " + user_name + " " + user_surname + ". You are " + str(age) +
      " years old. Your secret code is " + code + ".")
