import os
import importlib
import inspect
from base import BaseModule

def load_modules(log=0):
    modules_num = 0
    modules = {}
    for file in os.listdir("modules"):
        if file.endswith(".py") and file != "__init__.py":
            module_file_name = file[:-3]
            module = importlib.import_module(f"modules.{module_file_name}")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseModule) and obj is not BaseModule:
                    m = obj()
                    modules_num += 1
                    modules[modules_num] = m
                    if log:
                        print(f"""[+] Module '{m.name}' loaded""")
    return modules
