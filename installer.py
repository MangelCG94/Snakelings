import subprocess


def install():
    
    print("Checking python packages...")
    
    modules_list = subprocess.check_output(["pip","list"])
    
    if "termcolor".encode() not in modules_list:
        while True:
            print("The module 'termcolor' has yet to be installed.")
            sure = input("Do you want to install it? [y/N]")
            if sure.lower() == "y":
                subprocess.run(["pip","install","termcolor"])
                print("\nModule installed.\n\n")
                break
            elif sure.lower() == "n":
                print("\nInstallation terminated.\n")
                return 0;
            else :
                print("\n\n")
    else :
        print("\nThe python module 'termcolor' is already installed.")
    
    if "pytest".encode() not in modules_list:
        while True:
            print("The module 'pytest' has yet to be installed.")
            sure = input("Do you want to install it? [y/N]")
            if sure.lower() == "y":
                subprocess.run(["pip","install","pytest"])
                print("\nModule installed.\n\n")
                break
            elif sure.lower() == "n":
                print("\nInstallation terminated.\n")
                break
            else :
                print("\n\n")
    else :
        print("\nThe python module 'pytest' is already installed.")
    print("All done! Enjoy.")
    input("Click any key to continue...")