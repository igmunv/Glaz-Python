import sys
import os

import loader
from dicts.str_collector import *
from dicts.dictionary_main import *


modules = []


def launcher(module):

    VAR_VALUE = {}

    while True:

        var_value_input = input(f"{module.name}{DESIGNATIONS['input']}").strip()

        if not var_value_input:
            continue

        var_value = var_value_input.split()

        # Help
        if var_value[0] == "help":
            collect(var_value[0], data=module, skip_top=1, is_launcher=True)

        # Exit
        elif var_value[0] == "exit":
            collect("exit", is_launcher=True)
            return

        elif  var_value[0] == "run":

            # проверка на обязательную переменную
            is_mandatory_check_flag = False
            for var in module.variables:
                if module.variables[var]['is_mandatory'] and var not in VAR_VALUE:
                    collect("var_is_mand", data=var, is_launcher=True)
                    is_mandatory_check_flag = True
            if is_mandatory_check_flag:
                continue

            # присваивание None если переменной не присвоили значение

            for var in module.variables:
                if var not in VAR_VALUE:
                    VAR_VALUE[var] = None

            break

        elif len(var_value) == 2:
            var = var_value[0]
            value = var_value[1]
            if var in module.variables:
                # все значения которые передаются в модуль являются типом string
                VAR_VALUE[var] = value
            else:
                collect("var_is_n_found", is_launcher=True)

        else:
            collect("val_of_var_n_found", is_launcher=True)

    ret = module.run(VAR_VALUE)
    if ret == -1:
        collect("mod_error", is_launcher=True)
        return -1


def terminal_run():
    while (True):

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
    modules = loader.load_modules(1)

    # Run terminal
    terminal_run()


if __name__ == "__main__":
    main()
