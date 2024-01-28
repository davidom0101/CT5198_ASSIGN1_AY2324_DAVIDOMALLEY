'''
Student: David O'Malley
Module: CT5198
Assignment 1

This code does this following:
a. Creates a list to store the number of customers that a business had each day.

b. Uses a for loop to ask the user to input the number of customers each day over a 7vday period.

c. Determine the maximum, minimum and average number of customers for the week.
then prints the  results to the screen.
'''

def main():
    '''
    Main function
    '''
    # Initialize an empty list to store the user inuput
    num_customers = []

    # Get user input for each of the 7 days
    for day in range(1, 8):
        while True:  # This loop ensures that the user provides a valid input for each day
            user_input = input(
                f"Please enter the number of customers for day {day}: ")
            try:
                # Attempt to convert the input directly to an integer
                customers = int(user_input)

                # Check if the number is not negative
                if customers < 0:
                    print(
                        "Cannot be negative. Enter a valid integer.")
                    continue  # Prompt again for this day

                num_customers.append(customers)  # Add it to the list
                break  # Exit the loop for the current day
            except ValueError:
                # Prompt again if the input cannot be converted to an integer
                print("Invalid input. Please enter a whole number greater than zero")

    # Calculate and display results
    max_cust = max(num_customers)
    min_cust = min(num_customers)
    avg_cust = sum(num_customers) / len(num_customers)

    # Print the results
    print(f"\nMaximum number of customers in a day: {max_cust}")
    print(f"Minimum number of customers in a day: {min_cust}")
    print(f"Average number of customers per day: {avg_cust:.2f}")

if __name__ == "__main__":
    main()
