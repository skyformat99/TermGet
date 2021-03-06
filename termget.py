#!/usr/bin/env python3
import webbrowser, os, time, sys, getpass, urllib.request, hashlib, requests
from urllib import parse
# Colors (Thanks to Linux /usr/ for this code)
bold = "\033[1m"
reset = "\033[0m"
red = "\033[31m"
green = "\033[32m"
yellow = "\033[33m"
blue = "\033[34m"
magenta = "\033[35m"
cyan = "\033[36m"
print(reset) # disable all color on start

package = " "

# The TermGet SPLASHSCREEN
termgetBig = """
_________  _______   _______   _______   _______   _______  _________
\__   __/ (  ____ \ (  ____ ) (       ) (  ____ \ (  ____ \ \__   __/
   ) (    | (    \/ | (    )| | () () | | (    \/ | (    \/    ) (
   | |    | (__     | (____)| | || || | | |       | (__        | |
   | |    |  __)    |     __) | |(_)| | | | ____  |  __)       | |
   | |    | (       | (\ (    | |   | | | | \_  ) | (          | |
   | |    | (____/\ | ) \ \__ | )   ( | | (___) | | (____/\    | |
   )_(    (_______/ |/   \__/ |/     \| (_______) (_______/    )_(
"""

def multichoicePrompt(string):
    breakdoublereturn = string.split("\n\n") # top part is white bold, so split by double return will separate
    returnstr = reset + bold + breakdoublereturn[0] + "\n\n" # put top part in return
    mag = True # magenta? boolean

    for line in breakdoublereturn[1].split("\n"): # interlace the colors for each line
        if mag == True:
            returnstr = returnstr + bold + magenta + line + reset + "\n"
            mag = False
        else:
            returnstr = returnstr + bold + blue + line + reset + "\n"
            mag = True
    return returnstr + "\n" # final return (with extra newline) for function

try:
    try:
        package_file_read = open("/usr/local/share/termget/termget-package-manager", "r").read() # read package manager file
        # package_file_read = "" # debug feature
    except Exception:
        try:
            package_file_read = open("/usr/share/termget/termget-package-manager", "r").read() # read package manager file
        except Exception:
            print(yellow + "Warning: Missing Package File...")
    version = "3.0.0 Alpha1" # version number
    version_number = "1301"    # For each version number remove Beta or Alpha. alpha=1 beta=0 and remove all the dots for example: Alpha 1.1.0 would be 1110 Or Beta 1.1.1 would be 0111       **** !THIS IS USED FOR UPDATE SYSTEM! ****
    credit = magenta + (
        "TermGet was created by:\n"
        "- PizzaLovingNerd (main developer)\n"
        "- SadError256\n"
        "- Linux /usr/\n"
        "- Dylan Cruz\n"
        "- Emil Engler"
        )


    def setpack(var):
        os.system(' bash -c "echo -n ' + var + ' > /usr/local/share/termget/termget-package-manager"')

    def askreturn(): input(reset + yellow + "\nPress enter to continue")

    # Imports libraries and sets variables

    def pickManager():
        return multichoicePrompt(
            "\nPlease choose a package manager:\n"
            "\n1. apt-get (For Debian, and Debian based systems.)"
            "\n2. xbps (For Void Linux, and Void Linux based systems)"
            "\n3. dnf (For Fedora, and Fedora based systems)"
            "\n4. yum (For older versions of Fedora, and older Fedora based systems)"
            "\n5. zypper (For OpenSUSE, and OpenSUSE based systems)"
            "\n6. eopkg (For Solus, and Solus based systems)"
            "\n7. pacman (For Arch, and Arch based systems)"
            "\n8. emerge(For Gentoo, and Gentoo based systems)"
            "\n9. pkg (for FreeBSD, and FreeBSD based systems.)"
            "\n10. chromebrew (for Chrome OS, Chromium OS, CloudReady, and ZayuOS)"
            "\n11. homebrew (for macOS/Mac OS X)"
            "\n12. nix (For NixOS, and NixOS based systems.)"
        )

    if getpass.getuser() == "chronos":
        os.system("clear")
        setup = "True"
        while setup == "True":
            user = input(multichoicePrompt(
                "TermGet has detected this is Chrome OS, Chromium OS, CloudReady, or Nayu OS... is this true?\n"
                "\n1. Yes"
                "\n2. No"))

            if user == "1":
                setup = "False"
                package = "chromebrew"
            elif user == "2":
                setup = "False"
            else:
                print(red + "Error. Invalid answer")
                # Checks for Chromebook

    if package == " " and len(sys.argv) == 2:
        if sys.argv[1] == "apt-get" or sys.argv[1] == "apt" or sys.argv[2] == "apt" or sys.argv[1] == "apt-get": package = "apt-get"
        if sys.argv[1] == "pacman" or sys.argv[1] == "yaourt" or sys.argv[2] == "pacman" or sys.argv[2] == "yaourt": package = "pacman"
        if sys.argv[1] == "xbps" or sys.argv[2] == "xbps": package = "xbps"
        if sys.argv[1] == "dnf" or sys.argv[2] == "dnf": package = "dnf"
        if sys.argv[1] == "yum" or sys.argv[2] == "yum": package = "yum"
        if sys.argv[1] == "zypper" or sys.argv[2] == "zypper": package = "zypper"
        if sys.argv[1] == "eopkg" or sys.argv[2] == "eopkg": package = "eopkg"
        if sys.argv[1] == "pip3" or sys.argv[2] == "pip3": package = "pip3"
        if sys.argv[1] == "pip2" or sys.argv[2] == "pip2": package = "pip2"
        if sys.argv[1] == "pip" or sys.argv[2] == "pip": package = "pip"
        if sys.argv[1] == "apm" or sys.argv[2] == "apm": package = "apm"
        if sys.argv[1] == "emerge" or sys.argv[2] == "emerge": package = "emerge"
        if sys.argv[1] == "pkg" or sys.argv[2] == "pkg": package = "pkg"
        if sys.argv[1] == "chromebrew" or sys.argv[2] == "chromebrew": package = "chromebrew"
        if sys.argv[1] == "homebrew" or sys.argv[2] == "homebrew": package = "homebrew"
        if sys.argv[1] == "nix" or sys.argv[2] == "nix": package = "nix"
        if sys.argv[1] == "npm" or sys.argv[2] == "npm": package = "npm"
        if sys.argv[1] == "snap" or sys.argv[2] == "snap": package = "snap"
        if sys.argv[1] == "flatpak" or sys.argv[2] == "flatpak": package = "flatpak"
        if sys.argv[1] == "yarn" or sys.argv[2] == "yarn": package = "yarn"
        if sys.argv[1] == "appimage" or sys.argv[2] == "appimage": package = "appimage"
		if sys.argv[1] == "--list":
			list_enabled = True
			listfile = sys.argv[2]
			
    try:
        if package == " ":
            if package_file_read == "apt-get": package = "apt-get"
            elif package_file_read == "pacman": package = "pacman"
            elif package_file_read == "xbps": package = "xbps"
            elif package_file_read == "dnf": package = "dnf"
            elif package_file_read == "yum": package = "yum"
            elif package_file_read == "zypper": package = "zypper"
            elif package_file_read == "eopkg": package = "eopkg"
            elif package_file_read == "emerge": package = "emerge"
            elif package_file_read == "pkg": package = "pkg"
            elif package_file_read == "chromebrew": package = "chromebrew"
            elif package_file_read == "homebrew": package = "homebrew"
            elif package_file_read == "nix": package = "nix"
            print(reset + "package manager set to " + package)
    except Exception:
        print(yellow + "Warning: Missing Package File...")
        if package == " ": package = "null"
        print(reset + yellow + "package manager set to " + package)
    # Checks for command line argument


    def clear(): os.system("clear")
    # Runs "clear" over shell to clear the screen.

    clear()
    print(reset + bold + termgetBig + "\n\nThis is version " + version)

    if package == " " or package == "null":  # Checks for command line argument
        user = input(pickManager())
        setup = "True"
    else:
        time.sleep(1)
        clear()
        setup = "False"
        # Sets the variable 'setup' to False

    # Asks user which package manager to use

    while setup == "True":  # Repeats until setup is not true
        if user == "1":
            setup = "false"
            package = "apt-get"  # Sets package manager to apt-get
            setpack("apt-get")
        elif user == "2":
            setup = "false"
            package = "xbps"  # Sets package manager to xbps
            setpack("xbps")
        elif user == "3":
            setup = "false"
            package = "dnf"  # Sets package manager to dnf
            setpack("dnf")
        elif user == "4":
            setup = "false"
            package = "yum"  # Sets package manager to yum
            setpack("yum")
        elif user == "5":
            setup = "false"
            package = "zypper"  # Sets package manager to zypper
            setpack("zypper")
        elif user == "6":
            setup = "false"
            package = "eopkg"  # Sets package manager to eopkg
            setpack("eopkg")
        elif user == "7":
            setup = "false"
            package = "pacman"  # Sets package manager to pacman
            setpack("pacman")
        elif user == "8":
            setup = "false"
            package = "emerge"  # Sets package manager to emerge
            setpack("emerge")
        elif user == "9":
            setup = "false"
            package = "pkg"  # Sets package manager to pkg
            setpack("pkg")
        elif user == "10":
            setup = "false"
            package = "chromebrew"  # Sets package manager to chromebrew
            setpack("chromebrew")
        elif user == "11":
            setup = "false"
            package = "homebrew"
            setpack("homebrew")
        elif user == "12":
            setup = "false"
            package = "nix"
            setpack("nix")
        elif user == "13":
            setup = "false"
            package = "npm"
            setpack("npm")
        else:
            clear()
            print(red + "Error. Invalid package manager")
            time.sleep(1)
            clear()
            user = input(pickManager())
            # Sets package manager lolz

    # MEOW!

    if package != "pip" and package != "pip2" and package != "pip3" and package != "apm" and package != "npm" and package != "snap" and package != "flatpak" and package != "appimage":
        while True:  # Starts a loop
            clear()

            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Remove an application"
                "\n4. Update all packages"
                "\n5. Update Database"
                "\n6. Clean"
                "\n7. Credits"
                "\n8. Exit"
                "\n9. Enter shell"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print(reset + " ")
                if package == "apt-get": os.system("apt-cache search " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("pacman -Ss " + user)
                    if user1 == "2": os.system("yaourt -Ss " + user)
                elif package == "xbps": os.system("xbps-query -Rs " + user)
                elif package == "dnf": os.system("dnf search " + user)
                elif package == "yum": os.system("yum search " + user)
                elif package == "zypper": os.system("zypper search " + user)
                elif package == "eopkg": os.system("eopkg search " + user)
                elif package == "emerge": os.system("emerge -S " + user)
                elif package == "pkg": os.system("pkg search " + user)
                elif package == "chromebrew": os.system("crew search " + user)
                elif package == "homebrew": os.system("brew search " + user)
                elif package == "nix": os.system("nix search " + user)

                user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Please enter which package(s) to install: ")
                    print(reset + "")

                    if package == "apt-get": os.system("  apt-get install " + user)
                    elif package == "pacman":
                        user1 = input(multichoicePrompt(
                            "Which package manager would you like to use?\n"
                            "\n1. pacman"
                            "\n2. yaourt" + reset))
                        if user1 == "1": os.system("pacman -S " + user)
                        if user1 == "2": os.system("yaourt -S " + user)
                    elif package == "xbps": os.system("xbps-install " + user)
                    elif package == "dnf": os.system("dnf install " + user)
                    elif package == "yum": os.system("yum install " + user)
                    elif package == "zypper": os.system("zypper install " + user)
                    elif package == "eopkg": os.system("eopkg install " + user)
                    elif package == "emerge": os.system("emerge " + user)
                    elif package == "pkg": os.system("pkg install " + user)
                    elif package == "chromebrew": os.system("crew install " + user)
                    elif package == "homebrew": os.system("brew install " + user)
                    elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")

                if package == "apt-get": os.system("apt-get install " + user)
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt" + reset))
                    if user1 == "1": os.system("pacman -S " + user)
                    if user1 == "2": os.system("yaourt -S " + user)
                elif package == "xbps": os.system("xbps-install " + user)
                elif package == "dnf": os.system("dnf install " + user)
                elif package == "yum": os.system("yum install " + user)
                elif package == "zypper": os.system("zypper install " + user)
                elif package == "eopkg": os.system("eopkg install " + user)
                elif package == "emerge": os.system("emerge " + user)
                elif package == "pkg": os.system("pkg install " + user)
                elif package == "chromebrew": os.system("crew install " + user)
                elif package == "homebrew": os.system("brew install " + user)
                elif package == "nix": os.system("nix-env -i " + user)
                askreturn()

            if user == "3":  # Remove MEOW
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                        "How will you like to remove the package?\n"
                        "\n1. Remove, removes just the package (faster)"
                        "\n2. Purge, removes the package, and all it's configuration files (saves space)" + reset))
                    clear()
                    if user1 == "1": os.system("apt-get remove " + user)
                    if user1 == "2": os.system("apt-get purge " + user)
                elif package == "pacman": os.system("pacman -Rs " + user)
                elif package == "xbps": os.system("xbps-remove " + user)
                elif package == "dnf": os.system("dnf erase " + user)
                elif package == "yum": os.system("yum remove " + user)
                elif package == "zypper": os.system("zypper remove " + user)
                elif package == "eopkg": os.system("eopkg remove " + user)
                elif package == "emerge": os.system("emerge -C " + user)
                elif package == "pkg": os.system("pkg delete " + user)
                elif package == "chromebrew": os.system("crew remove " + user)
                elif package == "homebrew": os.system("brew uninstall " + user)
                elif package == "nix": os.system("nix-env -e " + user)
                askreturn()

            if user == "4":  # Updates Packages
                clear()
                if package == "apt-get":
                    user1 = input(multichoicePrompt(
                    "Do you also want to reload the database ?\n"
                    "\n1. Yes"
                    "\n2. No" + reset))
                    if user1 == "1": os.system("apt-get update")
                    os.system("apt-get upgrade")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt" + reset))
                    if user1 == "1": os.system("pacman -Syu")
                    if user1 == "2": os.system("yaourt -Syu --aur")
                elif package == "xbps": os.system("xbps-install -Su")
                elif package == "dnf":
                    os.system("dnf upgrade")
                    os.system("dnf distro-sync")
                elif package == "yum": os.system("yum update")
                elif package == "zypper":
                    os.system("zypper update && zypper up")
                    os.system("zypper dup")
                elif package == "eopkg": os.system("eopkg upgrade")
                elif package == "emerge":
                    os.system("emerge -u world")
                    os.system("emerge -uDN world")
                elif package == "pkg": os.system("pkg upgrade")
                elif package == "chromebrew": os.system("crew upgrade")
                elif package == "homebrew": os.system("brew upgrade")
                elif package == "nix": os.system("nix-env -u '*'")
                askreturn()

            if user == "5":  # Updates Database MEOW
                clear()
                if package == "apt-get": os.system("apt-get update")
                elif package == "pacman":
                    user1 = input(multichoicePrompt(
                        "Which package manager would you like to use?\n"
                        "\n1. pacman"
                        "\n2. yaourt"))
                    if user1 == "1": os.system("pacman -Syy")
                    if user1 == "2": os.system("yaourt -Syy" + reset)
                elif package == "xbps": os.system("xbps-install -S")
                elif package == "dnf": os.system("dnf clean expire-cache && dnf check-update")
                elif package == "zypper": os.system("zypper refresh zypper ref")
                elif package == "eopkg": os.system("eopkg ur")
                elif package == "emerge": os.system("layman -f")
                elif package == "yum": os.system("yum check-update")
                elif package == "pkg": os.system("pkg update")
                elif package == "chromebrew": print(reset + "This feature is unavailable for chromebrew\n")
                elif package == "homebrew": os.system("brew update")
                elif package == "nix": os.system("nix-channel --update nixpkgs")
                askreturn()

            if user == "6":  # Cleans

                clear()

                if package == "apt-get":
                    os.system("apt-get autoremove")
                    os.system("apt-get autoclean")
                    os.system("apt-get clean")
                elif package == "pacman":
                    os.system("pacman -Qdtq | pacman -Rs -")
                    os.system("pacman -Sc")
                elif package == "xbps":
                    os.system("xbps-remove -o")
                    os.system("xbps-remove -O")
                elif package == "dnf":
                    os.system("dnf autoremove")
                    os.system("dnf clean all")
                elif package == "yum":
                    os.system("yum clean all")
                    os.system("yum autoremove")
                elif package == "zypper":
                    os.system("zypper rm -u")
                    os.system("zypper clean")
                elif package == "eopkg":
                    os.system("eopkg delete-cache")
                    os.system("eopkg remove-orphans")
                elif package == "emerge":
                    os.system("emerge --depclean")
                    os.system("eclean distfiles")
                elif package == "pkg":
                    os.system("pkg clean")
                    os.system("pkg autoremove")
                elif package == "chromebrew": print(reset + "This feature is unavailable on chromebrew\n")
                elif package == "homebrew": print(reset + "Homebrew already does this automatically. :)\n")
                elif package == "nix": os.system("nix-collect-garbage -d")
                askreturn()
                         
            if user == "7":  # Credits

                clear()
                print(credit)
                time.sleep(3)

            if user == "8":
                print(reset)
                clear()
                quit()

            if user == "9":
                clear()
                print(reset + "Entering bash...")
                print(reset + "Press CTRL+D or type \"exit\" to return to termget.")
                os.system("bash")
                print(reset + "Returning to termget...")
                clear()
               
               
    if package == "pip" or package == "pip2" or package == "pip3":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed with pip"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print(reset + " ")
                os.system(package + " search \"" + user + "\"")

                user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Please enter which package(s) to install: ")
                    print(reset + "")

                    clear()
                    user = input(reset + "Please enter which package(s) to install: ")
                    print(reset + "")
                    os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print(reset + "")
                os.system(package + " install \"" + user + "\"")

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print(reset + "")
                os.system(package + " install --upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print(reset + "")
                os.system(package + " uninstall \"" + user + "\"")
                askreturn()

            if user == "5":  # List
                clear()
                print(reset + "")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system(package + " list ")
                if user == "2": os.system(package + " list --outdated")
                askreturn()

            if user == "6":  # Credits
                clear()
                print(credit)
                time.sleep(3)
                clear()

            if user == "7":
                print(reset)
                quit()

    if package == "apm":  # Starts a loop
        while True:
            clear()
            user = input(multichoicePrompt(
                "Please choose an action\n"
                "\n1. Search for packages"
                "\n2. Install an application"
                "\n3. Upgrade a package"
                "\n4. Remove an application"
                "\n5. List packages installed"
                "\n6. Credits"
                "\n7. Exit"))

            if user == "1":  # Search
                clear()
                user = input(reset + "Please enter search query: ")
                print("")
                os.system("apm search " + user)

                user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Please enter which package(s) to install: ")
                    print(reset + "")
                    os.system("apm install " + user)

                askreturn()

            if user == "2":  # Install
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print("")
                os.system("apm install " + user)

                askreturn()

            if user == "3":  # Upgrade
                clear()
                user = input(reset + "Please enter which package(s) to upgrade: ")
                print("")
                os.system(reset + "apm upgrade " + user)

                askreturn()

            if user == "4":  # Remove
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print("")
                os.system(reset + "apm uninstall" + user)

                askreturn()

            if user == "5":  # List
                clear()
                print("")
                user = input(multichoicePrompt(
                    "Please choose an action:\n"
                    "\n1. List all packages"
                    "\n2. List outdated packages"))
                if user == "1": os.system("apm list")
                if user == "2": os.system("apm outdated")
                askreturn()

            if user == "6":  # Credits - Meooow
                clear()
                print(credit)

                askreturn()

            if user == "7":
                print(reset)
                quit()

    if package == "snap":
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "\n1. Search for snaps"
            "\n2. Install a snap"
            "\n3. Remove a snap"
            "\n4. List installed snaps"
            "\n5. Credits"
            "\n6. Exit"))

            if user == "1":
                clear()
                user = input(reset + "Please enter search query: ")
                print("")
                os.system(reset + "snap find " + user)

                user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Please enter which package(s) to install: ")
                    print("")
                    os.system(reset + "snap install " + user)
                    
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print("")
                os.system(reset + "snap install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Please enter which package(s) to remove: ")
                print("")
                os.system(reset +  "snap remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("The current installed snaps are: ")
                os.system(reset + "snap list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()



    if package == "flatpak":
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "\n1. Search for flatpak (On flathub)"
            "\n2. Install a flatpak (On flathub)"
            "\n3. Remove a flatpak"
            "\n4. List installed flatpak"
            "\n5. Credits"
            "\n6. Exit"))

            if user == "1":
                clear()
                user = input(reset + "Please enter search query: ")
                print("")
                os.system(reset + "flatpak search " + user)

                user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                if user == "y" or user == "Y":
                    clear()
                    user = input(reset + "Please enter which flatpak(s) to install")
                    print("")
                    os.system(reset + "flatpak install flathub " + user)
                    askreturn()


                askreturn()
            if user == "2":
                clear()
                user = input(reset + "Please enter which flatpak(s) to install")
                print("")
                os.system(reset + "flatpak install flathub " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Please enter which flatpak(s) to remove: ")
                print("")
                os.system(reset +  "flatpak remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("The current installed flatpaks are: ")
                os.system(reset + "flatpak list")
                askreturn()

            if user == "5":
                clear()
                credits()

            if user == "6":
                print(reset)
                quit()


    if package == "yarn" or package == "npm":
        pkg_dir = input(reset + "Enter the path of your js project: ")
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "\n1. Search for package"
            "\n2. Install a package"
            "\n3. Remove a package"
            "\n4. List installed packages"
            "\n5. Update all local packages"
            "\n5. Credits"
            "\n6. Exit"))

            if user == "1":
                clear()
                print("")
                if package == "npm":
                    user = input(reset + "Please enter a search query: ")
                    os.system("npm search " + user)
                    user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                    if user == "y" or user == "Y":
                        os.system("npm install " + user)
                        askreturn()

                elif package == "yarn":
                    print("Yarn doesn't have a search function built in. Would you like to search with your default browser? (y/n)")
                    if user == "y" or "Y":
                        user = input(reset + "Input a search query: ")
                        webbrowser.open_new("https://yarnpkg.com/en/packages?q=" + user + "&p=1")
                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Please enter which package(s) to install: ")
                print("")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm install " + user)
                if package == "yarn": os.system("yarn install " + user)
                askreturn()

            if user == "3":
                clear()
                user = input(reset + "Please enter which package(s) to remove ")
                print("")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm uninstall " + user)
                elif package == "yarn": os.system("yarn remove " + user)
                askreturn()

            if user == "4":
                clear()
                print("The current installed packages are: ")
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm ls")
                elif package == "yarn": os.system("yarn list")
                askreturn()

            if user == "5":
                clear()
                os.chdir(pkg_dir)
                if package == "npm": os.system("npm update")
                if package == "yarn": os.system("yarn update")
                askreturn()

            if user == "6":
                clear()
                credits()

            if user == "7":
                print(reset)
                quit()

    if package == "appimage":
        while True:
            clear()
            user = input(multichoicePrompt(
            "Please choose an action:\n"
            "\n1. Search for AppImage"
            "\n2. Download a AppImage"
            "\n3. Credits"
            "\n4. Exit"))

            if user == "1":
                clear()
                user = input(reset + "Input a search query: ")
                print("")
                
                url = 'https://appimage.github.io/feed.json'
                r = requests.get(url)
                data = r.json()['items']

                appimage_name = input('Name: ')
                appimage_exists = False
                for entry in data:

                    if entry['name'].lower() == appimage_name.lower(): #we found it!
                            
                        try: #check if url exists
                            appimage_release_url = entry['links'][-1]['url']
                            appimage_exists = True
                            print(f'The package has been "{appimage_name}" has been found. Would you like to install it?')
                            
                            user = input(yellow + "\nDid you find what you were looking for? (y/n)" + reset)

                            if user == "y" or user == "Y":
                            
                                print(f"url: {appimage_release_url}")
                                appimage_download_url = appimage_release_url.replace('github.com', 'api.github.com/repos') + "/latest"
                                print("Downloading AppImage...")
                                os.system('mkdir ~/Applications \
                                | cd ~/Applications \
                                | curl -s ' + appimage_download_url + ' \
                                | grep "browser_download_url.*AppImage" \
                                | cut -d : -f 2,3 \
                                | tr -d \\" \
                                | wget -qi -')
                                print("Done!")

                        except TypeError: #No link
                            print(f'The AppImage "{appimage_name}" doesn\'t have a download URL. This means that it is probably not hosted on GitHub. Unfortunately, this TermGet only works with GitHub releases of AppImages')

                        
                if appimage_exists == False:
                    print(f'The AppImage "{appimage_name}" doesn\'t exist. If an AppImage is missing, please report it to AppImageHub.')

                askreturn()

            if user == "2":
                clear()
                user = input(reset + "Please enter which AppImage(s) to download ")
                print("")
                
                url = 'https://appimage.github.io/feed.json'
                r = requests.get(url)
                data = r.json()['items']

                appimage_name = input('Name: ')
                appimage_exists = False
                for entry in data:

                    if entry['name'].lower() == appimage_name.lower(): #we found it!
                            
                        try: #check if url exists
                            appimage_exists = True
                            appimage_release_url = entry['links'][-1]['url']
                            print(f"url: {appimage_release_url}")
                            appimage_download_url = appimage_release_url.replace('github.com', 'api.github.com/repos') + "/latest"
                            print("Downloading AppImage...")
                            os.system('mkdir ~/Applications \
                            | cd ~/Applications \
                            | curl -s ' + appimage_download_url + ' \
                            | grep "browser_download_url.*AppImage" \
                            | cut -d : -f 2,3 \
                            | tr -d \\" \
                            | wget -qi -')
                            print("Done!")

                        except TypeError: #No link
                            print(f'The AppImage "{appimage_name}" doesn\'t have a download URL. This means that it is probably not hosted on GitHub. Unfortunately, this TermGet only works with GitHub releases of AppImages')

                        
                if appimage_exists == False:
                    print(f'The AppImage "{appimage_name}" doesn\'t exist. If an AppImage is missing, please report it to AppImageHub.')
                askreturn()

            if user == "3":
                clear()
                credits()

            if user == "4":
                print(reset)
                quit()
						 
except KeyboardInterrupt:
        clear()
        print(red + "Error: Keyboard Interuption. Quitting" + reset) # moo
        quit()
