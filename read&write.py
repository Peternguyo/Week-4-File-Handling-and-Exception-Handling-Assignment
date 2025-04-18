def modify_and_write_file(input_filename, output_filename):
    """
    Reads a text file, modifies its content (converts to uppercase),
    and writes the modified content to a new file.

    Args:
        input_filename (str): The name of the input file to read.
        output_filename (str): The name of the output file to write to.
    """
    try:
        with open(input_filename, 'r') as infile:
            file_content = infile.read()
            modified_content = file_content.upper()

        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Successfully read '{input_filename}', modified it, and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred while processing '{input_filename}': {e}")

if __name__ == "__main__":
    while True:
        input_file = input("Enter the name of the file you want to process: ")
        output_file = "modified_" + input_file  # Create a default output filename

        try:
            # Attempt to open the file in read mode to check if it exists and is readable
            with open(input_file, 'r') as test_read:
                pass  # If we reach here, the file exists and is readable
            break  # Exit the loop if the file is accessible
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist. Please enter a valid filename.")
        except PermissionError:
            print(f"Error: Permission denied to read '{input_file}'. Please check file permissions.")
        except Exception as e:
            print(f"An unexpected error occurred while trying to access '{input_file}': {e}")

    modify_and_write_file(input_file, output_file)