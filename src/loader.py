import os
import importlib
import inspect

from base import BaseModule
import builder


# Modules Loader
def load_modules():

    # Modules are stored
    modules = {}

    # Get script dir
    glaz_dir = os.path.dirname(os.path.abspath(__file__))

    # Get modules
    modules_path = f"{glaz_dir}/modules"
    files = os.listdir(modules_path)
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
                    main_class = obj()

                    # If dependencies need to be built
                    if main_class.build == True:

                        # Check: Are the dependencies built?
                        is_build_path = f"{modules_path}/{module_dir}/.is_build.glaz"

                        if not os.path.exists(is_build_path):

                            # * If the dependencies need to be rebuilt, delete the.is_build.glaz file in the module directory
                            # * Если зависимости необходимо скомпилировать заново то удалите файл .is_build.glaz в директории модуля

                            builder.build(main_class, modules_path, module_dir, is_build_path)



                    # Add module in result
                    modules[len(modules)+1] = main_class
                    print(f"[+] Module {main_class.name} loaded")

        except ModuleNotFoundError:
            pass

    return modules
