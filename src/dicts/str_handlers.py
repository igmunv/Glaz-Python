from dicts.dictionary_main import *
import dicts.dictionary_main as ddm



#
# EXAMPLE
#

def example(lang_lib, data=None):

    result = f"YOUR TEXT"

    return result



#
# MAIN (TERMINAL)
#

def help_(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['main_help_output_begin']}\n"

    for cmd in ddm.COMMANDS:
        cmd_vars = ', '.join(ddm.COMMANDS[cmd])
        result += f"{ddm.DESIGNATIONS['border']} {cmd_vars} - {lang_lib.DESC_COMMANDS[cmd]}\n"

    return result


def exit_(lang_lib, data=None):

    result = f"{lang_lib.TEXTS['exit']}"

    return result


def modules(lang_lib, data=None):

    modules = data

    result = f"{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['modules_output_begin']}\n"

    for module in modules:
        result += f"{ddm.DESIGNATIONS['border']} {module}. '{modules[module].name}'\n"

    result += f"\n{lang_lib.TEXTS['modules_output_end']}"

    return result


def unknow_command(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['unknow_command']}"

    return result


def unknow_module(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['modules_not_found']}"

    return result


def module_load(lang_lib, data=None):

    # Module name in variable 'data'
    module_name = data

    result = f"{ddm.DESIGNATIONS['add']} {lang_lib.TEXTS['module_load_p1']} '{module_name}' {lang_lib.TEXTS['module_load_p2']}"

    return result

#
# LAUNCHER
#

def help_launcher(lang_lib, data=None):

    # Module information in variable 'data'
    module = data

    result = f"{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['main_help_output_begin']}\n"

    for cmd in ddm.LAUNCHER_COMMANDS:
        cmd_vars = ', '.join(ddm.LAUNCHER_COMMANDS[cmd])
        result += f"{ddm.DESIGNATIONS['border']} {cmd_vars} - {lang_lib.DESC_LAUNCHER_COMMANDS[cmd]}\n"

    result += f"\n{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['success']} {module.name}:\n"

    mandatory_variables = {}
    optional_variables = {}
    for var in module.variables:
        if module.variables[var]['is_mandatory']:
            mandatory_variables[var] = module.variables[var]
        else:
            optional_variables[var] = module.variables[var]

    if len(mandatory_variables) > 0 or len(optional_variables) > 0:
        result += f"{ddm.DESIGNATIONS['border']}\n"

    if len(mandatory_variables) > 0:
        result += f"{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['module_run_mand_vars_begin']}\n"

        for var in mandatory_variables:
            result += f"{ddm.DESIGNATIONS['border']} {var} : {module.variables[var]['description']}\n"

    if len(mandatory_variables) > 0 and len(optional_variables) > 0:
        result += f"{ddm.DESIGNATIONS['border']}\n"

    if len(optional_variables) > 0:
        result += f"{ddm.DESIGNATIONS['border']} {ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['module_run_optn_vars_begin']}\n"

        for var in optional_variables:
            result += f"{ddm.DESIGNATIONS['border']} {var} : {module.variables[var]['description']}\n"

    if len(mandatory_variables) > 0 or len(optional_variables) > 0:
        result += f"\n{lang_lib.TEXTS['module_run_vars_end']}"

    return result


def exit_launcher(lang_lib, data=None):

    result = f"Back to Glaz..."

    return result


def value_of_variable_not_found(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['module_run_value_not_found']}"

    return result


def module_error(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['module_run_module_return_error']}"

    return result


def module_finish(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['info']} {lang_lib.TEXTS['module_run_module_finish_work']}"

    return result


def variable_is_not_found(lang_lib, data=None):

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['module_run_var_not_found']}"

    return result


def variable_is_mandatory(lang_lib, data=None):

    # Variable name in data
    var_name = data

    result = f"{ddm.DESIGNATIONS['error']} {lang_lib.TEXTS['module_run_var_is_mand_p1']} '{var_name}' {lang_lib.TEXTS['module_run_var_is_mand_p2']}"

    return result

