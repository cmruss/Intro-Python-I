# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even():
    print(num % 2 == 0)

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

is_even()

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def is_even():
    if num % 2 == 0:
        print("Even!")
    else: 
        print("Odd")

is_even()
