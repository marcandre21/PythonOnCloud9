# The following block of code will only be executed if this script is run as the main program
if __name__ == '__main__':
    # Get the number of commands (N) from the user
    N = int(input())
    
    # Initialize an empty list
    the_list = list()

    # Loop through N commands
    for _ in range(N):
        # Get the user input as a space-separated string and split it into a list of strings
        query = input().split()

        # Check the command type and perform the corresponding operation
        if query[0] == "print":
            # Print the current state of the list
            print(the_list)
        elif query[0] == "insert":
            # Insert the specified value at the specified index
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            # Remove the specified value from the list
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            # Append the specified value to the end of the list
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            # Sort the list in ascending order
            the_list = sorted(the_list)
        elif query[0] == "pop":
            # Remove and return the last element from the list
            the_list.pop()
        elif query[0] == "reverse":
            # Reverse the order of elements in the list
            the_list.reverse()