import time
import random
import os
from colorama import Fore, init

# Initialize colorama
init()

# ASCII artwork
ascii_art = """
 ██████   ██████ █████ ██████   █████ █████       ███████████  ███████████      ███████          █████ ██████████   █████████  ███████████
░░██████ ██████ ░░███ ░░██████ ░░███ ░░███       ░░███░░░░░███░░███░░░░░███   ███░░░░░███       ░░███ ░░███░░░░░█  ███░░░░░███░█░░░███░░░█
 ░███░█████░███  ░███  ░███░███ ░███  ░███        ░███    ░███ ░███    ░███  ███     ░░███       ░███  ░███  █ ░  ███     ░░░ ░   ░███  ░ 
 ░███░░███ ░███  ░███  ░███░░███░███  ░███        ░██████████  ░██████████  ░███      ░███       ░███  ░██████   ░███             ░███    
 ░███ ░░░  ░███  ░███  ░███ ░░██████  ░███        ░███░░░░░░   ░███░░░░░███ ░███      ░███       ░███  ░███░░█   ░███             ░███    
 ░███      ░███  ░███  ░███  ░░█████  ░███        ░███         ░███    ░███ ░░███     ███  ███   ░███  ░███ ░   █░░███     ███    ░███    
 █████     █████ █████ █████  ░░█████ █████       █████        █████   █████ ░░░███████░  ░░████████   ██████████ ░░█████████     █████   
░░░░░     ░░░░░ ░░░░░ ░░░░░    ░░░░░ ░░░░░       ░░░░░        ░░░░░   ░░░░░    ░░░░░░░     ░░░░░░░░   ░░░░░░░░░░   ░░░░░░░░░     ░░░░░    
"""

# List of colors
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Function to display the ASCII artwork with random colors for a specified duration
def display_ascii_art_with_random_colors(ascii_art, duration):
    start_time = time.time()
    while time.time() - start_time < duration:
        # Choose a random color
        color = random.choice(colors)

        # Print the ASCII artwork with the chosen color
        print(color + ascii_art, end="\r")

        # Wait for a short time before changing the color
        time.sleep(0.9)

    # Reset the color to default
    print(Fore.RESET)

# Display the ASCII artwork with random colors for 10 seconds
display_ascii_art_with_random_colors(ascii_art, 2)

 # Clear the console after the last frame is printed
os.system('cls' if os.name == 'nt' else 'clear')
