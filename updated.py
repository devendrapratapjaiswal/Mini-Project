import mp
import nm
import os
import subprocess
from colorama import Fore, Style, init

# Initialize colorama for Windows compatibility
init(autoreset=True)

# List of essential utilities including programming languages and compilers
ESSENTIAL_UTILITIES = {
    "General Development": ["build-essential", "gcc", "make", "cmake"],
    "Python Development": ["python3", "python3-pip", "python3-venv"],
    "Node.js Development": ["nodejs", "npm"],
    "Ruby Development": ["ruby", "gem"],
    "C/C++ Development": ["gcc", "g++", "make"],
    "Java Development": ["default-jdk", "maven"],
    "PHP Development": ["php", "composer"],
    "Go Development": ["golang"],
    "Networking Tools": ["curl", "net-tools", "nmap"],
    "System Monitoring": ["htop", "sysstat", "iotop"],
    "Web Development": ["apache2", "nginx", "php", "mysql-server"],
    "Security Tools (Kali)": ["nmap", "wireshark", "aircrack-ng", "john", "hydra"]
}

def display_message(message, color=Fore.YELLOW, end_line=True):
    """Helper function to display a formatted message with color."""
    print(color + message + Style.RESET_ALL)
    if end_line:
        print(Fore.LIGHTBLACK_EX + "." * 50 + Style.RESET_ALL)  # dotted line separator

def detect_linux_distribution():
    try:
        with open("/etc/os-release") as f:
            for line in f:
                if line.startswith("ID="):
                    distro = line.split("=")[1].strip().replace('"', '')
                    return distro.lower()
    except FileNotFoundError:
        return None

def get_package_manager():
    distro = detect_linux_distribution()
    if distro in ["ubuntu", "debian", "kali"]:
        return "apt"
    elif distro in ["arch", "manjaro"]:
        return "pacman"
    elif distro in ["fedora", "centos", "rhel"]:
        return "dnf"
    return None

def install_package(package_manager, package):
    if package_manager == "apt":
        command = ["sudo", "apt", "install", package, "-y"]
    elif package_manager == "pacman":
        command = ["sudo", "pacman", "-S", package, "--noconfirm"]
    elif package_manager == "dnf":
        command = ["sudo", "dnf", "install", package, "-y"]
    else:
        display_message(f"Unsupported package manager: {package_manager}", Fore.RED)
        return False

    display_message(f"Installing {package} using {package_manager}...", Fore.CYAN)
    try:
        subprocess.run(command, check=True)
        display_message(f"{package} installed successfully!", Fore.GREEN)
        return True
    except subprocess.CalledProcessError:
        display_message(f"Failed to install {package}.", Fore.RED)
        return False

def scan_system(package_manager):
    display_message("Scanning system for missing essential utilities...", Fore.CYAN)

    missing_tools = []
    installed_tools = ""
    if package_manager == "apt":
        installed_tools = subprocess.run(["dpkg", "-l"], capture_output=True, text=True).stdout
    elif package_manager == "pacman":
        installed_tools = subprocess.run(["pacman", "-Q"], capture_output=True, text=True).stdout
    elif package_manager == "dnf":
        installed_tools = subprocess.run(["dnf", "list", "installed"], capture_output=True, text=True).stdout
    else:
        display_message("Unsupported package manager.", Fore.RED)
        return

    for category, tools in ESSENTIAL_UTILITIES.items():
        for tool in tools:
            if tool not in installed_tools:
                missing_tools.append((category, tool))

    if missing_tools:
        display_message("The following essential utilities are missing on your system:", Fore.YELLOW)
        for category, tool in missing_tools:
            display_message(f"Category: {category}, Tool: {tool}", Fore.YELLOW, end_line=False)
            install_choice = input(Fore.LIGHTCYAN_EX + f"Do you want to install {tool}? (y/n): " + Style.RESET_ALL).strip().lower()
            if install_choice == 'y':
                install_package(package_manager, tool)
    else:
        display_message("Your system has all the essential utilities installed!", Fore.GREEN)

def scan_programming_languages(package_manager):
    display_message("Scanning system for missing programming language dependencies...", Fore.CYAN)

    missing_languages = []
    checks = [
        (["python3", "--version"], "Python Development"),
        (["node", "--version"], "Node.js Development"),
        (["ruby", "--version"], "Ruby Development"),
        (["gcc", "--version"], "C/C++ Development"),
        (["java", "--version"], "Java Development"),
        (["php", "--version"], "PHP Development"),
        (["go", "version"], "Go Development"),
    ]

    for command, lang in checks:
        try:
            subprocess.run(command, check=True, capture_output=True)
        except subprocess.CalledProcessError:
            missing_languages.append(lang)

    if missing_languages:
        display_message("The following programming language dependencies are missing:", Fore.YELLOW)
        for lang in missing_languages:
            display_message(f"Category: {lang}", Fore.YELLOW, end_line=False)
            install_choice = input(Fore.LIGHTCYAN_EX + f"Do you want to install the tools for {lang}? (y/n): " + Style.RESET_ALL).strip().lower()
            if install_choice == 'y':
                for tool in ESSENTIAL_UTILITIES[lang]:
                    install_package(package_manager, tool)
    else:
        display_message("All essential programming language tools are installed!", Fore.GREEN)

def show_main_menu():
    print("\n" + Fore.LIGHTBLUE_EX + "\033[1m*** - LINUX SMART UTILITY MANAGER - ***\033[0m\n" + Style.RESET_ALL)
    print(Fore.LIGHTCYAN_EX + "\033[1mChoose an option:\033[0m\n" + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Update the system")
    print(Fore.RED + "2. Upgrade the system")
    print(Fore.CYAN + "3. Install predefined utilities")
    print(Fore.BLUE + "4. Scan system for missing utilities")
    print(Fore.GREEN + "5. Scan for missing programming language dependencies")
    print("6. Exit" + Style.RESET_ALL)
    print(Fore.LIGHTBLACK_EX + "-" * 50 + Style.RESET_ALL)

def update_system(package_manager):
    display_message("Updating the system...", Fore.CYAN)
    command = []
    if package_manager == "apt":
        command = ["sudo", "apt-get", "update"]
    elif package_manager == "pacman":
        command = ["sudo", "pacman", "-Syu"]
    elif package_manager == "dnf":
        command = ["sudo", "dnf", "check-update"]
    try:
        subprocess.run(command, check=True)
        display_message("System updated successfully!", Fore.GREEN)
    except subprocess.CalledProcessError:
        display_message("Error: Unable to update the system.", Fore.RED)

def upgrade_system(package_manager):
    display_message("Upgrading the system...", Fore.CYAN)
    command = []
    if package_manager == "apt":
        command = ["sudo", "apt-get", "full-upgrade", "-y"]
    elif package_manager == "pacman":
        command = ["sudo", "pacman", "-Syu"]
    elif package_manager == "dnf":
        command = ["sudo", "dnf", "upgrade", "-y"]
    try:
        subprocess.run(command, check=True)
        display_message("System upgraded successfully!", Fore.GREEN)
    except subprocess.CalledProcessError:
        display_message("Error: Unable to upgrade the system.", Fore.RED)

def main():
    package_manager = get_package_manager()
    if not package_manager:
        display_message("Unsupported Linux distribution or package manager.", Fore.RED)
        return

    while True:
        show_main_menu()
        choice = input(Fore.LIGHTCYAN_EX + "\nEnter your choice (1-6): " + Style.RESET_ALL).strip()

        if choice == '1':
            update_system(package_manager)
        elif choice == '2':
            upgrade_system(package_manager)
        elif choice == '3':
            category = input(Fore.LIGHTCYAN_EX + "\nEnter the category of tools to install (e.g., Python Development): " + Style.RESET_ALL).strip()
            if category in ESSENTIAL_UTILITIES:
                for tool in ESSENTIAL_UTILITIES[category]:
                    install_package(package_manager, tool)
            else:
                display_message(f"Invalid category: {category}.", Fore.RED)
        elif choice == '4':
            scan_system(package_manager)
        elif choice == '5':
            scan_programming_languages(package_manager)
        elif choice == '6':
            display_message("Exiting the program. Goodbye!", Fore.LIGHTBLUE_EX)
            break
        else:
            display_message("Invalid choice. Please try again.", Fore.RED)

if __name__ == "__main__":
    main()

