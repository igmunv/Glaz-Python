import sys
import os

import loader
from dicts.str_collector import *
from dicts.dictionary_main import *


# Modules are stored
modules = []


# Module Launcher
def launcher(module):

    # Variables for module
    VAR_VALUE = {}

    while True:

        # User Input
        var_value_input = input(f"{module.name}{DESIGNATIONS['input']}").strip()

        # Empty: re-input
        if not var_value_input:
            continue

        # Split: var and value (for variables)
        var_value = var_value_input.split()

        # Help: Output all commands and module variables
        if var_value_input in LAUNCHER_COMMANDS['help']:
            collect(var_value_input, data=module, skip_top=1, is_launcher=True)

        # Exit: back to Glaz
        elif var_value_input in LAUNCHER_COMMANDS['exit']:
            collect("exit", is_launcher=True)
            return

        # Run: run module
        elif var_value_input in LAUNCHER_COMMANDS['run']:

            # Check: var is required?
            is_mandatory_check_flag = False
            for var in module.variables:
                if module.variables[var]['is_required'] and var not in VAR_VALUE:
                    collect("var_is_mand", data=var, is_launcher=True)
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
            collect("mod_finish", is_launcher=True)

            # Module error
            if module_return == -1:
                collect("mod_error", is_launcher=True)
                return -1

            break;

        # If user set value for var
        elif len(var_value) == 2:

            var = var_value[0]
            value = var_value[1]

            if var in module.variables:
                VAR_VALUE[var] = value  # Type values for module: string
            else:
                collect("var_is_n_found", is_launcher=True)

        # Unknow command
        else:
            collect("val_of_var_n_found", is_launcher=True)

    collect("exit", is_launcher=True)

# Main Terminal
def terminal():
    while (True):

        # User Input
        command = input(f"{DESIGNATIONS['input']}").strip()

        # Empty: re-input
        if not command:
            continue

        # Help: Output all commands
        if command in COMMANDS['help']:
            collect(command, skip_top=1)

        # Exit: Exit from Glaz
        elif command in COMMANDS['exit']:
            collect(command)
            sys.exit(0)

        # Modules: Output all loaded modules
        elif command in COMMANDS['modules']:
            collect(command, data=modules, skip_top=1)

        # Number: Run launcher for selected module
        elif command.isdigit():

            # Module is not found
            if int(command) not in modules:
                collect("unknow_module")

            # Run launcher
            else:
                module = modules[int(command)]
                launcher(module)

        # Other: Unknow command
        else:
            collect(command)


def main():

    # Load modules
    global modules
    modules = loader.load_modules()

    # Run terminal
    terminal()


if __name__ == "__main__":
    main()
