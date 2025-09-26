import sys

from commands import *

#
# TERMINAL
#

# help
def help_terminal_handler():

    print()
    print(f"| [*] All commands:")

    for cmd in COMMANDS:
        cmd_vars = ', '.join(COMMANDS[cmd])
        print(f"| {cmd_vars} - {DESC_COMMANDS[cmd]}")
    print()

# exit
def exit_terminal_handler():
    print("Exit...")
    sys.exit(0)

# modules
def modules_terminal_handler(modules):

    print()
    print(f"| [*] All loaded modules:")

    for module_num in modules:
        print(f"| {module_num}. '{modules[module_num].name}'")

    print()
    print("Enter the number to run module")

#
# LAUNCHER
#

# help
def help_launcher_handler(module):


    # Commands block

    print()

    print(f"| [*] All commands:")

    for cmd in LAUNCHER_COMMANDS:
        cmd_vars = ', '.join(LAUNCHER_COMMANDS[cmd])
        print(f"| {cmd_vars} - {DESC_LAUNCHER_COMMANDS[cmd]}")

    print()

    print(f"| [v] {module.name}:")

    # Variables block

    required_variables = {}
    optional_variables = {}
    for var in module.variables:
        if module.variables[var]['is_required']:
            required_variables[var] = module.variables[var]
        else:
            optional_variables[var] = module.variables[var]

    if len(required_variables) > 0 or len(optional_variables) > 0:
        print(f"|")

    if len(required_variables) > 0:
        print(f"| [*] Required variables:")

        for var in required_variables:
            print(f"| {var} : {module.variables[var]['description']}")

    if len(required_variables) > 0 and len(optional_variables) > 0:
        print(f"|")

    if len(optional_variables) > 0:
        print(f"| [*] Optional variables:")

        for var in optional_variables:
            print(f"| {var} : {module.variables[var]['description']}")

    print()

    if len(required_variables) > 0 or len(optional_variables) > 0:
        print(f"Enter 'VARIABLE VALUE' to assign a value to a variable. Example: 'host http://192.168.0.1/'")

    print()
