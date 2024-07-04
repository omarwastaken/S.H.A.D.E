### This tool is intended for educational purposes only. 
### Please be aware that using it for any illegal activity is strictly prohibited and at your own risk. 
### I take no responsibility for any misuse of this project.
### S.H.A.D.E © 2024 by Omar Badawy is licensed under CC BY-NC 4.0 

# ============= Imports =============
from modules.visuals import display_ascii_art, show_intro, thinking_animation
from modules.prompt_api import generate_combined_prompt, generate_password_batches
from modules.utils import handle_exceptions, write_wordlist_to_file, count_passwords
from colorama import Fore


# ============= Main Function =============
def main():
    # Display ASCII art and introduction
    display_ascii_art()
    show_intro()

    while True:
        # Get user input for known passwords
        passwords_input = input(Fore.BLUE + "Please enter known passwords related to victim (space-separated, leave empty to skip): ")
        # Get user input for victim details
        details_input = input(Fore.BLUE + "Please enter details related to victim (comma-separated, leave empty to skip): ")
        # Get user input for important numbers or dates
        numbers_input = input(Fore.BLUE + "Please enter numbers or dates related to victim (comma-separated, leave empty to skip): ")
        
        # Ask if the user wants to add custom generation rules
        custom_rules_choice = input(Fore.BLUE + "Would you like to add custom generation rules? (Y/N): ").strip().lower()
        custom_rules = ""
        if custom_rules_choice == 'y':
            # Get user input for custom rules if they chose 'yes'
            custom_rules = input(Fore.BLUE + "Describe the custom rules to apply: ")

        # Get user input for the number of batches to generate
        batches_input = int(input(Fore.BLUE + "How many batches of ~30 passwords do you want to generate? "))
        print("\n")
        
        try:
            # Generate the combined prompt based on user input
            combined_prompt = generate_combined_prompt(details_input, numbers_input, passwords_input, custom_rules)
            # Generate the password batches
            all_passwords = generate_password_batches(combined_prompt, batches_input)
            
            # Combine all passwords into a single wordlist
            final_wordlist = "\n".join(all_passwords)
            
            # Write the final wordlist to a file
            write_wordlist_to_file(final_wordlist)
            
            # Count the number of passwords generated
            password_count = count_passwords(final_wordlist)
            print(Fore.GREEN + f"\n{password_count} passwords generated!")
            print(Fore.GREEN + "Wordlist saved to output/wordlist.txt")
            
        except Exception as e:
            handle_exceptions(e)

        # Ask if the user wants to run the tool again
        repeat_choice = input(Fore.BLUE + "\nWould you like to generate a wordlist for another victim? (Y/N): ").strip().lower()
        if repeat_choice != 'y':
            print(Fore.MAGENTA + "Exiting S.H.A.D.E. Thank you for using the tool.")
            break

if __name__ == "__main__":
    main()
