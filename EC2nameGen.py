"""
EC2 name generator 
"""
import random
import string

def generate_unique_names(num_instances, dept_name):
    names = []
    for _ in range(num_instances):
        # Generate a random string of characters and numbers
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        
        # Combine department name and random string to create a unique name
        unique_name = f"{dept_name}_{random_string}"
        
        # Append the unique name to the list
        names.append(unique_name)
    
    return names

def main():
    # Get user input for the number of instances and department name
    num_instances = int(input("Enter the number of EC2 instances: "))
    dept_name = input("Enter the name of your department: ")
    
    # Generate unique names
    unique_names = generate_unique_names(num_instances, dept_name)
    
    # Print the generated unique names
    print("\nGenerated unique names:")
    for name in unique_names:
        print(name)

if __name__ == "__main__":
    main()