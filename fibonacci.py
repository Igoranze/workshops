"""
The Fibonacci Sequence is the series of numbers:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it.

The 2 is found by adding the two numbers before it (1+1)
The 3 is found by adding the two numbers before it (1+2),
And the 5 is (2+3),
and so on!
"""


def run():
    """
    Start Fibonacci from this function
    """

    # Fibonacci always starts at 1, but we need to enter the range here:
    # We should add type checking here INT
    max_iterations = int(input('Enter the number of iterations: '))

    # Create an empty array to store our Fibonacci results in
    fibonacci_array = []

    # Python does not have a for( int i = 0; ) so we need to hack our way into this type of for loop
    # We also need an extra value to keep track of our iterations
    iteration = 0
    i = 0
    while iteration < max_iterations:
        # Add the first value
        first = i

        # Add the second value
        second = i + 1

        # Add first + second
        result = first + second

        fibonacci_array.append([first, second, result])

        # Set i to be result + 1
        i = result + 1

        # Update our loop iteration
        iteration += 1

    # Print our fibonacci array
    print(fibonacci_array)


# Starting function, use:
# python fibonacci.py
run()
