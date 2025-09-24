import sys
import os
import importlib

import loader

glaz_dir = os.path.dirname(os.path.abspath(__file__))
LANG = open(f"{glaz_dir}/dicts/language", encoding="utf-8").read().strip()
lang_module_name = f"dicts.dictionary_{LANG}"

modules = []

def module_run(module):
    print()
    print(f"{module.name}")
    print(f"{module.description}")

    # print("| variable: description")
    # print("| All variables:")

    mandatory_variables = {}
    optional_variables = {}
    for var in module.variables:
        if module.variables[var]['is_mandatory']:
            mandatory_variables[var] = module.variables[var]
        else:
            optional_variables[var] = module.variables[var]

    print("| [*] Mandatory variables:")
    for var in mandatory_variables:
        print(f"| {var}: MANDATORY : {module.variables[var]['description']}")
    print("|")
    print("| [*] Optional variables:")
    for var in optional_variables:
        print(f"| {var}: OPTIONAL : {module.variables[var]['description']}")

    print("Enter 'VARIABLE VALUE' to assign a value to a variable. Example: 'host http://192.168.0.1/'")
    print("")
    print("Enter 'exit' for back to Glaz")
    print("Enter 'run' for run module")

    VAR_VALUE = {}


    while True:
        var_value_input = input(f"{module.name} > ")

        if len(var_value_input) > 0:
            var_value = var_value_input.split()

            if var_value[0] == "exit":
                print("Back to Glaz...")
                return
            if  var_value[0] == "run":

                # проверка на обязательную переменную
                is_mandatory_check_flag = False
                for var in module.variables:
                    if module.variables[var]['is_mandatory'] and var not in VAR_VALUE:
                        print(f"[!] Variable '{var}' is mandatory!")
                        is_mandatory_check_flag = True
                if is_mandatory_check_flag:
                    continue

                # присваивание None если переменной не присвоили значение

                for var in module.variables:
                    if var not in VAR_VALUE:
                        VAR_VALUE[var] = None

                break

            if len(var_value) == 2:
                var = var_value[0]
                value = var_value[1]
                if var in module.variables:
                    # все значения которые передаются в модуль являются типом string
                    VAR_VALUE[var] = value
                else:
                    print('[!] Variable is not found!')

            else:
                print('[!] Enter value of variable!')

    ret = module.run(VAR_VALUE)
    if ret == -1:
        print("[!] Module error")
        return -1

def terminal_run():
    while (True):

        command = input(" > ").strip()


        if command in COMMANDS['help']['varieties']:
            print()
            print("| [*] All commands:")
            for cmd in COMMANDS:
                cmd_vars = ', '.join(COMMANDS[cmd]['varieties'])
                print(f"| {cmd_vars} - {COMMANDS[cmd]['description']}")


        elif command in COMMANDS['exit']['varieties']:
            print("Exit...")
            sys.exit(0)


        elif command in COMMANDS['modules']['varieties']:
            print()
            print("| [*] All loaded modules:")
            for module in modules:
                print(f"| {module}. '{modules[module].name}'")
            print()
            print("Enter the number to run module")


        elif command.isdigit():
            if int(command) not in modules:
                print("Модуль с таким номером не загружен. Чтобы посмотреть загруженные модули введите 'module'")
            else:
                module = modules[int(command)]
                module_run(module)


        else:
            if len(command) > 0:
                print(f"{DESIGNATION['error']} {TEXT['unknow_command']}")

def main():
    global modules
    modules = loader.load_modules(1)
    terminal_run()

if __name__ == "__main__":
    mod = importlib.import_module(lang_module_name)
    globals().update(vars(mod))
    main()
