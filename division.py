# Exception handling / error handling

# try except block - try catch block
# else block, finally block


# can create error class - must be a child class of exception class
class NegativeError(Exception):
    pass # it will inherit the functionality and thus doesn't require any methods
    # To use this, you would put "raise NegativeError" instead of example below
    # OR can put "except NegativeError as err: print(err)"

try:
    n = int(input("Enter a numerator: "))
    d = int(input("Enter a denominator: "))

    # If we don't want negative numbers
    if (n < 0 or d < 0):
        raise Exception("No negative numbers please")

    q = n / d

    print(q)

except Exception as err:
# can also make this specific -- except ZeroDivisionError -- this will catch ONLY zero div error
    print(type(err))
    print("Something went wrong!")

print("End of the program")

# An example where a "finally" block may be appropriate:

# try:
    # open a file
    # write something - it may throw error
# except:
    # handle the error
# finally:
    # close the file
