# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
# When "" is blank it means (enter)
keep_going = ""
while keep_going == "":

    # Get width and height and check they are more than zero
    width = num_check("Width: ")
    height = num_check("Height: ")
    cost = num_check("cost/m: ")

    # Calculate perimeter and te price for the fence
    perimeter = 2 * (width + height)
    price = (perimeter * cost)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Price: ${price:.2f}")

    keep_going = input("Press <enter> to keep going or any key to quit.")