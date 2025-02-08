# Write a function that accepts a list of numbers as an argument
# And returns list with squares for each number
def square_lst(numbers):
    result = []
    for num in numbers:
        result.append(num ** 2)
    return result


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = square_lst(x)
print(y)

# Write a function that accepts a list of numbers
# And returns a tuple with two numbers, amount of odd and even numbers
# Example: input -> [1, 2, 3, 4, 5] output (3, 2)
# Where 3 is amount of Odds and 2 is amount of evens
def count_odds_and_evens(lst):
    odds = 0
    evens = 0
    for num in lst:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1
    return odds, evens


y = count_odds_and_evens(x)
print(y)


# Write a function that accepts a list of numbers
# and returns largest number
def find_largest(nums):
    return max(nums)


y = find_largest(x)
print(y)


# Write a function that accepts a start number and end number
# Create a FizzBuzz for given range
# (If number divided by 3 has no remainder, print number + FIZZ
# If number divided by 5 has no remainder, print number + BUZZ
# If number divided by 5 and 3 has no remainder, print number + FIZZBUZZ)
def fizzbuzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')


fizzbuzz(-20, 50)