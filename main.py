import os
import sys

def CmdTB():
    commands = {
        0: 'start cmd',
        1: 'start regedit',
        2: 'start powershell',
        3: 'msinfo32',
        4: 'exit'
    }

    print("\nChoix :")
    print("--------")
    print("Command Prompt (CMD): 0")
    print("Regedit (REG): 1")
    print("PowerShell (PWSHELL): 2")
    print("Msinfo32 (MSINFO32): 3")
    print("Quitter: 4")
    print("--------")

    try:
        choice = int(input("Votre choix : "))
        if choice in commands:
            if choice == 4:
                sys.exit(0)
            os.system(commands[choice])
        else:
            print("Choix invalide. Veuillez réessayer.")
    except ValueError:
        print("Entrée non valide. Veuillez entrer un nombre.")
    
    os.system('cls')

if __name__ == "__main__":
    while True:
        CmdTB()

