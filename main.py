from termcolor import colored, cprint
import pytest

import time

import installer
import tests.test_variables1 as testvar_one



# make this more like rustlings?
def main() :
    
    intro = "Welcome to Snakelings."
    # should it show the whole message everytime?

    cprint(intro, "cyan")

    installer.install()
    calling()


def calling() :
    testvar_one.test_exercise()


if __name__ == "__main__":
    main()


#time.sleep(5)
