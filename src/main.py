import sys

import loader



def main():

    modules = loader.load_modules(1)


    while (True):
        command = input(" > ")

        if command == "help":
            print("")
        elif command == "exit":
            sys.exit()

        elif command == "modules":
            print()
            print("[*] All loaded modules:")
            for module in modules:
                print(f"| {module}. '{modules[module].name}'")
            print()

        elif command.isdigit():
            if int(command) not in modules:
                print("Модуль с таким номером не загружен. Чтобы посмотреть загруженные модули введите 'module'")
            else:
                print(f"'{modules[int(command)].name}'")


if __name__ == "__main__":
    main()
