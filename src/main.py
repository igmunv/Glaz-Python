import sys

import loader

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
    print("| [*] Optional variables:")
    for var in optional_variables:
        print(f"| {var}: OPTIONAL : {module.variables[var]['description']}")

    print("Enter 'VARIABLE VALUE' to assign a value to a variable. Example: 'host 192.168.0.1'")
    print("")
    print("Enter 'exit' for back to Glaz")
    print("Enter 'run' for run module")

    VAR_VALUE = {}


    # как указывать обязательна ли переменная?


    while True:
        var_value_input = input(f"{module.name} > ")

        if len(var_value_input) > 0:
            var_value = var_value_input.split()

            if var_value[0] == "exit":
                print("Back to Glaz...")
                return
            if  var_value[0] == "run":
                break

            if len(var_value) == 2:
                var = var_value[0]
                value = var_value[1]
                if var in module.variables:
                    # все значения которые передаются в модуль являются типом string
                    VAR_VALUE[var] = value

            else:
                print('Enter value of variable!')

    module.run(VAR_VALUE)

def terminal_run():
    while (True):
        command = input(" > ")

        if command == "help":
            print("")
        elif command == "exit":
            print("Exit...")
            sys.exit()

        elif command == "modules":
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
                print("[!] Unknow command. Enter 'help' to view commands")

def main():
    global modules
    modules = loader.load_modules(1)
    terminal_run()

if __name__ == "__main__":
        main()
