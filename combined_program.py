# combined_program.py
def modify_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        modified_content = content.upper()  # Example modification
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        
        print(f"File has been successfully modified and saved to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"Error: An I/O error occurred. {e}")

def read_file_with_error_handling():
    filename = input("Enter the filename you want to open: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of the file '{filename}':\n")
            print(content)
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError as e:
        print(f"Error: Unable to read the file. {e}")

# Run the combined version
filename = input("Enter the filename you want to modify: ")
read_file_with_error_handling()  # Handle errors before modifying

output_filename = "modified_" + filename
modify_file_content(filename, output_filename)  # Modify and write the file
