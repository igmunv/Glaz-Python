import os
import importlib
import inspect
from base import BaseModule

from dicts.str_collector import *
from dicts.dictionary_main import *


# Modules Loader
def load_modules():

    # Modules are stored
    modules = {}

    # Get script dir
    glaz_dir = os.path.dirname(os.path.abspath(__file__))

    # Get modules path
    files = os.listdir(f"{glaz_dir}/modules")
    module_dirs = []
    for file in files:
        if os.path.isdir(f"{glaz_dir}/modules/{file}"):
            module_dirs.append(file)

    # Get base class of modules
    for module_dir in module_dirs:
        try:

            # import module
            module = importlib.import_module(f"modules.{module_dir}.main")

            # add module if contains Glaz Based Class (BaseModule in '/base.py' file)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                if issubclass(obj, BaseModule) and obj is not BaseModule:
                    m = obj()
                    modules[len(modules)+1] = m
                    collect("module_load", data=m.name)
        except ModuleNotFoundError:
            pass

    return modules
