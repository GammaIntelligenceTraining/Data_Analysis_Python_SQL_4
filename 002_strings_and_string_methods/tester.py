string_sample1 = "Hello world world"
                # 0123456
                        #-5-4-3-2-1
string_sample2 = "fiRst lEtTer is lowErCase"
string_sample3 = "** extra spacing   !!!  "
german_sample = "der Fluß"

# [START:END:STEP]
# print(string_sample1[len(string_sample1)-1])
# print(string_sample1[10:16])

# print(string_sample1[-5:-1])
# print(string_sample1[12:])
# print(string_sample1[::-2])

# print(string_sample1.upper())
# print(german_sample.lower())
# print(german_sample.casefold())
#
# print(string_sample1.title())
# print(string_sample1.capitalize())
#
# print(string_sample3.rstrip(' *!'))

# print(string_sample1.replace(' ', '', 1))

# print(string_sample1.count('o', 0, 7))

# print(string_sample1.find('o'))
# print('hello'.center(30, '*'))

# print('1234'.zfill(10))

# salary = 1000
# string = 'Johns salary is {1}. {1} {1} {1} {1}.'
#
# print(string.format(salary, True))

price = 1500
string = "This {product} costs ${price:,.2f} {number:+}."
print(string.format(product="computer", price=price, number=123))


# # Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)
#
# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500
#
# emp_string = ('Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f'
#               % {'name': emp_name, 'salary': emp_salary, 'age': emp_age})
# print(emp_string)

name = "jack"
surname = 'smith'
salary = 1500

print(f"Hello {name.title()} {surname.title()}. Your salary is {salary * 0.78:.2f}.")
#
# print('hello world'.encode('utf16'))
# print(b'\xff\xfeh\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00'.decode('utf16'))

print(r'\n means new line')

print(r'C:\Users\User\PycharmProjects\Data_Analysis_Python_SQL_4\002_strings_and_string_methods\002_string_methods_2.py')
