# Print to console what is different in each set compared to another
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.difference(set_b))
print(set_b.difference(set_a))
print(set_a - set_b)

# Create a string from a list and save it to variable
# Make each name on a new line.
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
names_string = "\n".join(names)
print(names_string)


# print sum of all numbers in a list
# print sum of all unique numbers in a list
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
# print(sum(numbers))
# print(sum(set(numbers)))

nums_sum = 0
unique_sum = 0
for num in numbers:
    if type(num) is int or type(num) is float:
        nums_sum += num

# for num in set(numbers):
#     unique_sum += num
print(nums_sum)
print(unique_sum)

# create a new list from studentsA and studentsB
# make sure there is no duplicates in a new lists
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']
# new = list(set(studentsA + studentsB))
# print(new)
# new = []
# for name in studentsA:
#     if name not in new:
#         new.append(name)
# for name in studentsB:
#     if name not in new:
#         new.append(name)
#
# print(new)



# What elements are common for both tuples?
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)
print(set(numbersA).intersection(set(numbersB)))
print(set(numbersA) & set(numbersB))

# add 5 to the tuple on a right position
a = (1, 2, 3, 4, 6, 7, 8)
# a = *a[:4], 5, *a[4:]
# a = a[:4] + (5,) + a[4:]
# a = (1, 2, 3, 4) + (5,) + (5, 6, 7)
# a = list(a)
# a.insert(4, 5)
# a.append(5)
# a.sort()
# a = tuple(a)
# print(a)

# # add 5 after 31
# b = (6, 4, 31, 76, 23, 13)
# x = 5
# b = list(b)
# b.insert(b.index(31) + 1, x)
# b = tuple(b)
# print(b)
