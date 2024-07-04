# ============= Imports =============
import os
from colorama import Fore
from datetime import datetime

# ============= Exception Handling =============
def handle_exceptions(exception):
    # Handle exceptions and print the error message
    print(Fore.RED + f"\nAn unexpected error occurred: {exception}")

# ============= Directory Management =============
def create_output_directory():
    # Create the output directory if it doesn't exist
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

# ============= File Writing =============
def write_wordlist_to_file(wordlist):
    # Write the wordlist to a file with a timestamped filename
    output_dir = create_output_directory()
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f"wordlist_{current_time}.txt")
    with open(output_file, "w") as file:
        file.write(wordlist)
    print(Fore.GREEN + f"Wordlist saved to {output_file}")

# ============= Password Counting =============
def count_passwords(wordlist):
    # Count the number of passwords in the wordlist
    return len(wordlist.splitlines())
