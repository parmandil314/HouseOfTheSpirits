import os

def clear():
    """ Clear the screen """
    if os.name == "posix":
        os.environ["TERM"] = "xterm-256color"
        os.system("clear")  # POSIX-compatible Unix
    else:
        os.system("cls")    # Windows