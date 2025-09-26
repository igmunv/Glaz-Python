import sys
import os

import loader
from command_handlers import *


# Modules are stored
modules = []


# Module Launcher
def launcher(module):

    # Variables for module
    VAR_VALUE = {}

    while True:

        # User Input
        var_value_input = input(f"{module.name} > ").strip()

        # Empty: re-input
        if not var_value_input:
            continue

        # Split: var and value (for variables)
        var_value = var_value_input.split()

        # Help: Output all commands and module variables
        if var_value_input in LAUNCHER_COMMANDS['help']:
            help_launcher_handler(module)

        # Exit: back to Glaz
        elif var_value_input in LAUNCHER_COMMANDS['exit']:
            break

        # Run: run module
        elif var_value_input in LAUNCHER_COMMANDS['run']:

            # Check: var is required?
            is_mandatory_check_flag = False
            for var in module.variables:
                if module.variables[var]['is_required'] and var not in VAR_VALUE:
                    print(f"Variable '{var}' is required!")
                    is_mandatory_check_flag = True
            if is_mandatory_check_flag:
                continue

            # If user not set value for variable: variable value = None
            for var in module.variables:
                if var not in VAR_VALUE:
                    VAR_VALUE[var] = None

            # Run
            module_return = module.run(VAR_VALUE)

            # Finish
            print("[*] Module finished work")

            # Module error
            if module_return == -1:
                print("[!] Module error!")
                return -1

            # Exit from launcher
            break;

        # If user set value for var
        elif len(var_value) == 2:

            var = var_value[0]
            value = var_value[1]

            if var in module.variables:
                VAR_VALUE[var] = value  # Type values for module: string
            else:
                print("[!] Variable is not found!")

        # Unknow command
        else:
            print(f"[!] Enter value of variable! Enter '{LAUNCHER_COMMANDS['help'][0]} to view commands and usage!")

    print("Back to Glaz...")

# Main Terminal
def terminal():
    while (True):

        # User Input
        command = input(f" > ").strip()

        # Empty: re-input
        if not command:
            continue

        # Help: Output all commands
        if command in COMMANDS['help']:
            help_terminal_handler()

        # Exit: Exit from Glaz
        elif command in COMMANDS['exit']:
            exit_terminal_handler()

        # Modules: Output all loaded modules
        elif command in COMMANDS['modules']:
            modules_terminal_handler(modules)

        # Number: Run launcher for selected module
        elif command.isdigit():

            # Module is not found
            if int(command) not in modules:
                print(f"A module with this number is not loaded! Type '{COMMANDS['modules'][0]}' to view the modules")

            # Run launcher
            else:
                module = modules[int(command)]
                launcher(module)

        # Other: Unknow command
        else:
            print(f"Unknow command! Enter '{COMMANDS['help'][0]}' to view commands")


def main():

    # Load modules
    global modules
    modules = loader.load_modules()

    # Run terminal
    terminal()


if __name__ == "__main__":
    main()
