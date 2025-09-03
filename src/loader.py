import os
import importlib
import inspect
from base import BaseModule

def load_modules(log=0):
    modules_num = 0
    modules = {}

    files = os.listdir("modules")
    module_dirs = []
    for file in files:
        if os.path.isdir(f"modules/{file}"):
            module_dirs.append(file)

    for module_dir in module_dirs:
        try:
            module = importlib.import_module(f"modules.{module_dir}.main")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseModule) and obj is not BaseModule:
                    m = obj()
                    modules_num += 1
                    modules[modules_num] = m
                    if log:
                        print(f"""[+] Module '{m.name}' loaded""")
        except ModuleNotFoundError:
            pass

    return modules
