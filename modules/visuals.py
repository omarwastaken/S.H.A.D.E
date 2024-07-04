# ============= Imports =============
import pyfiglet 
from colorama import init, Fore
import itertools
import threading
import time

# ============= Initialization =============
# Initialize colorama for colored text output
init(autoreset=True)

# ============= Display Functions =============
def display_ascii_art():
    # Generate and display ASCII art for S.H.A.D.E.
    shade_art = pyfiglet.figlet_format("S.H.A.D.E.", font="isometric3")
    subtitle = "Skight's Hacker AI-Driven Engine\n"
    separator = "-" * 80
    byline = "\nCreated by Omar Badawy\n"
    github_link = "GitHub: https://github.com/omarwastaken\n"
    print(Fore.GREEN + shade_art)
    print(Fore.LIGHTGREEN_EX + subtitle)
    print(Fore.YELLOW + separator)
    print(Fore.CYAN + byline)
    print(Fore.CYAN + github_link)
    print(Fore.YELLOW + separator)

def show_intro():
    # Display introductory information about S.H.A.D.E.
    print(Fore.MAGENTA + "\nWelcome to S.H.A.D.E. - Skight's Hacker AI-Driven Engine\n")
    print(Fore.MAGENTA + "\nDescription: S.H.A.D.E. is an AI-powered tool developed to generate comprehensive password wordlists.")
    print(Fore.MAGENTA + "By analyzing natural language provided details based on the victim, it creates targeted specially curated wordlists")
    print(Fore.MAGENTA + "to aid in ethical hacking and cybersecurity testing.\n")
    print(Fore.RED + "Disclaimer: This tool is for ethical purposes only. Use it responsibly.\n")    
    print(Fore.MAGENTA + "Let's get started!\n\n")

# ============= Animation Functions =============
def thinking_animation(message):
    # Display a "thinking" animation
    global stop_anim
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_anim:
            break
        print(Fore.YELLOW + f'\r{message} ' + c, end='', flush=True)
        time.sleep(0.1)

def start_thinking_animation(message):
    # Start the thinking animation in a separate thread
    global stop_anim
    stop_anim = False
    anim_thread = threading.Thread(target=thinking_animation, args=(message,))
    anim_thread.start()
    return anim_thread

def stop_thinking_animation(anim_thread, message, batch_number):
    # Stop the thinking animation and display completion message
    global stop_anim
    stop_anim = True
    anim_thread.join()
    clear_message = " " * (len(message) + 5)
    print(Fore.GREEN + f'\r{clear_message}', end='', flush=True)
    print(Fore.GREEN + f"\rGenerating Batch {batch_number}: " + Fore.LIGHTGREEN_EX + "Complete ✔")
