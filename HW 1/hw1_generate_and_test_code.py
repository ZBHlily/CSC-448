# Problem:
# Generate and Test Paradigm
# Suppose you must determine whether a given number between 3 and 100 inclusively is a prime. Recall that an integer N ≥ 2 is prime if its only factors are 1 and itself. So 17 and 23 are primes whereas 33 is not, because it is the product of 3 and 11.

# Assume that you must solve this problem without benefit of a computer or pocket calculator. Your first attempt at a solution, using the generate-and-test approach, might look like the following pseduocode:

# {While the problem is not yet solved and more possible factors for Number
# remain:
#     [Generate a possible factor for Number
#     /* possible factors will be generated in the order 2, 3, 4, 5, ... Number*/
#     Test: if (Number)/(possible factor) is an integer >= 2
#     Then return not prime]
# End While}
# If possible factor equals Number,
# Then return Number is prime


# function to check if a number is prime
def is_prime_number(n):
  # prime numbers are greater than or equal to 2
  if n < 2:
    return False

  # checks for factors of the number to see if it is a prime number
  for i in range(2, n):
    # if a factor is found --> then the number is not prime
    if n % i == 0:
      return False

  # if no factors are found the number is prime
  return True


# test case to test the function for numbers between 3 and 100
for num in range(3, 101):
  if is_prime_number(num):
    print(f"{num} is a prime number.")
  else:
    print(f"{num} is not a prime number.")

# second test case for user input
start_range = int(input("\nEnter the starting number of the range: "))
end_range = int(input("Enter the ending number of the range: "))

# tests the function for the user specified range
for num in range(start_range, end_range + 1):
  if is_prime_number(num):
    print(f"{num} is a prime number.")
  else:
    print(f"{num} is not a prime number.")